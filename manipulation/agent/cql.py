from sqlite3 import adapt
import hydra
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import OrderedDict

import utils
from dm_control.utils import rewards
import wandb


class Actor(nn.Module):
    def __init__(self, obs_dim, action_dim, hidden_dim):
        super().__init__()

        self.policy = nn.Sequential(nn.Linear(obs_dim, hidden_dim),
                                    nn.LayerNorm(hidden_dim), nn.Tanh(),
                                    nn.Linear(hidden_dim, hidden_dim),
                                    nn.ReLU(inplace=True),
                                    nn.Linear(hidden_dim, 2 * action_dim))

        self.apply(utils.weight_init)

    def forward(self, obs):
        mu, log_std = self.policy(obs).chunk(2, dim=-1)

        mu = torch.tanh(mu)
        std = log_std.clamp(-10, 2).exp()

        dist = utils.SquashedNormal(mu, std)
        return dist

class MuActor(nn.Module):
    def __init__(self, obs_dim, action_dim, hidden_dim):
        super().__init__()

        self.policy = nn.Sequential(nn.Linear(obs_dim, hidden_dim),
                                    nn.LayerNorm(hidden_dim), nn.Tanh(),
                                    nn.Linear(hidden_dim, hidden_dim),
                                    nn.ReLU(inplace=True),
                                    nn.Linear(hidden_dim, 2 * action_dim))

        self.apply(utils.weight_init)

    def forward(self, obs):
        mu, log_std = self.policy(obs).chunk(2, dim=-1)
        std = log_std.clamp(-10, 2).exp()
        dist = utils.TruncatedNormal(mu, std)
        return dist



class Critic(nn.Module):
    def __init__(self, obs_dim, action_dim, hidden_dim):
        super().__init__()

        self.q1_net = nn.Sequential(
            nn.Linear(obs_dim + action_dim, hidden_dim),
            nn.LayerNorm(hidden_dim), nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, 1))

        self.q2_net = nn.Sequential(
            nn.Linear(obs_dim + action_dim, hidden_dim),
            nn.LayerNorm(hidden_dim), nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(inplace=True),
            nn.Linear(hidden_dim, 1))

        self.apply(utils.weight_init)

    def forward(self, obs, action):
        obs_action = torch.cat([obs, action], dim=-1)
        q1 = self.q1_net(obs_action)
        q2 = self.q2_net(obs_action)

        return q1, q2


class CQLAgent:
    def __init__(self,
                 name,
                 obs_shape,
                 action_shape,
                 device,
                 lr,
                 hidden_dim,
                 critic_target_tau,
                 nstep,
                 batch_size,
                 use_tb,
                 alpha,
                 n_samples,
                 target_cql_penalty,
                 use_critic_lagrange,
                 has_next_action=False,
                 method=False,
                 method_type=0,
                 method_temp=20,
                 method_alpha=0.5,
                 **kwargs
        ):
        self.action_dim = action_shape[0]
        self.hidden_dim = hidden_dim
        self.lr = lr
        self.device = device
        self.critic_target_tau = critic_target_tau
        self.use_tb = use_tb
        self.use_critic_lagrange = use_critic_lagrange
        self.target_cql_penalty = target_cql_penalty

        self.alpha = alpha
        self.n_samples = n_samples

        # models
        self.actor = Actor(obs_shape[0], action_shape[0],
                           hidden_dim).to(device)

        self.mu_actor = MuActor(obs_shape[0], action_shape[0],
                            hidden_dim).to(device)

        self.critic = Critic(obs_shape[0], action_shape[0],
                             hidden_dim).to(device)
        self.critic_target = Critic(obs_shape[0], action_shape[0],
                                    hidden_dim).to(device)
        self.critic_target.load_state_dict(self.critic.state_dict())

        # method
        self.method = method
        self.method_type = method_type
        self.method_temp = method_temp
        self.method_alpha = method_alpha
        self.neg_adv = True if method_type in [1] else False

        # lagrange multipliers
        self.target_entropy = -self.action_dim
        self.log_actor_alpha = torch.zeros(1,
                                           requires_grad=True,
                                           device=device)
        self.log_critic_alpha = torch.zeros(1,
                                            requires_grad=True,
                                            device=device)

        # optimizers
        self.actor_opt = torch.optim.Adam(self.actor.parameters(), lr=lr)
        self.mu_opt = torch.optim.Adam(self.mu_actor.parameters(), lr=lr)
        self.critic_opt = torch.optim.Adam(self.critic.parameters(), lr=lr)
        self.actor_alpha_opt = torch.optim.Adam([self.log_actor_alpha], lr=lr)
        self.critic_alpha_opt = torch.optim.Adam([self.log_critic_alpha], lr=lr)

        config = {
            'name': name,
            'obs_shape': obs_shape,
            'action_shape': action_shape,
            'device': device,
            'lr': lr,
            'hidden_dim': hidden_dim,
            'critic_target_tau': critic_target_tau,
            'nstep': nstep,
            'batch_size': batch_size,
            'use_tb': use_tb,
            'alpha': alpha,
            'n_samples': n_samples,
            'target_cql_penalty': target_cql_penalty,
            'use_critic_lagrange': use_critic_lagrange,
            'has_next_action': has_next_action,
            'method': method,
            'method_type': method_type,
            'method_temp': method_temp,
            'method_alpha': method_alpha,
            'neg_adv': self.neg_adv,
        }

        # wandb.config.update(config)

        self.train()
        self.critic_target.train()

    def train(self, training=True):
        self.training = training
        self.actor.train(training)
        self.critic.train(training)

    def act(self, obs, step, eval_mode):
        obs = torch.as_tensor(obs, device=self.device).unsqueeze(0)
        policy = self.actor(obs)
        if eval_mode:
            action = policy.mean
        else:
            action = policy.sample()
            if step < self.num_expl_steps:
                action.uniform_(-1.0, 1.0)
        return action.cpu().numpy()[0]

    def _repeated_critic_apply(self, obs, actions):
        """
            obs is (batch_size, obs_dim)
            actions is (n_samples, batch_size, action_dim)

            output tensors are (n_samples, batch_size, 1)
        """
        batch_size = obs.shape[0]
        n_samples = actions.shape[0]

        reshaped_actions = actions.reshape((n_samples * batch_size, -1))
        repeated_obs = obs.unsqueeze(0).repeat((n_samples, 1, 1))
        repeated_obs = repeated_obs.reshape((n_samples * batch_size, -1))

        Q1, Q2 = self.critic(repeated_obs, reshaped_actions)
        Q1 = Q1.reshape((n_samples, batch_size, 1))
        Q2 = Q2.reshape((n_samples, batch_size, 1))

        return Q1, Q2

    def update_critic(self, obs, action, reward, discount, next_obs, step):
        metrics = dict()

        # Compute standard SAC loss
        with torch.no_grad():
            dist = self.actor(next_obs)
            sampled_next_action = dist.sample()
            target_Q1, target_Q2 = self.critic_target(next_obs,
                                                      sampled_next_action)
            target_V = torch.min(target_Q1, target_Q2)
            target_Q = reward + (discount * target_V)

        Q1, Q2 = self.critic(obs, action)
        critic_loss = F.mse_loss(Q1, target_Q) + F.mse_loss(Q2, target_Q)

        # Add CQL penalty
        with torch.no_grad():
            random_actions = torch.FloatTensor(self.n_samples, Q1.shape[0],
                                               action.shape[-1]).uniform_(
                                                   -1, 1).to(self.device)
            sampled_actions = self.actor(obs).sample(
                sample_shape=(self.n_samples,))
            next_sampled_actions = self.actor(next_obs).sample(
                sample_shape=(self.n_samples,))
            
            mu_actions = self.mu_actor(obs).sample(
                sample_shape=(self.n_samples,))

        rand_Q1, rand_Q2 = self._repeated_critic_apply(obs, random_actions)
        sampled_Q1, sampled_Q2 = self._repeated_critic_apply(
            obs, sampled_actions)
        next_sampled_Q1, next_sampled_Q2 = self._repeated_critic_apply(
            obs, next_sampled_actions)
        mu_Q1, mu_Q2 = self._repeated_critic_apply(obs, mu_actions)

        cat_Q1 = torch.cat(
            [rand_Q1, sampled_Q1, next_sampled_Q1,
             Q1.unsqueeze(0)], dim=0)
        cat_Q2 = torch.cat(
            [rand_Q2, sampled_Q2, next_sampled_Q2,
             Q2.unsqueeze(0)], dim=0)

        cql_logsumexp = torch.logsumexp(
            cat_Q1,
            dim=0,
        ).mean() + torch.logsumexp(
            cat_Q2,
            dim=0,
        ).mean()

        if self.method_type in [0]:
            mu_logsumexp = torch.logsumexp(mu_Q1, dim=0).mean() + torch.logsumexp(mu_Q2, dim=0).mean()
            cql_logsumexp = self.method_alpha * cql_logsumexp + (1 - self.method_alpha) * mu_logsumexp
        elif self.method_type in [1]:
            mu_dist = self.mu_actor(obs)
            mu_sampled_next_action = mu_dist.sample()
            mu_Q1, mu_Q2 = self.critic(obs, mu_sampled_next_action)
            Q1 = self.method_alpha * Q1 + (1 - self.method_alpha) * mu_Q1
            Q2 = self.method_alpha * Q2 + (1 - self.method_alpha) * mu_Q2

        cql_penalty = cql_logsumexp - (Q1 + Q2).mean()

        # Update lagrange multiplier
        if self.use_critic_lagrange:
            alpha = torch.clamp(self.log_critic_alpha.exp(),
                                min=0.0,
                                max=1000000.0)
            alpha_loss = -0.5 * alpha * (cql_penalty - self.target_cql_penalty)

            self.critic_alpha_opt.zero_grad()
            alpha_loss.backward(retain_graph=True)
            self.critic_alpha_opt.step()
            alpha = torch.clamp(self.log_critic_alpha.exp(),
                                min=0.0,
                                max=1000000.0).detach()
        else:
            alpha = self.alpha

        # Combine losses
        critic_loss = critic_loss + alpha * cql_penalty

        # optimize critic
        self.critic_opt.zero_grad()
        critic_loss.backward()
        self.critic_opt.step()

        metrics['critic_target_q'] = target_Q.mean().item()
        metrics['critic_q1'] = Q1.mean().item()
        metrics['critic_q2'] = Q2.mean().item()
        metrics['critic_loss'] = critic_loss.item()
        metrics['critic_cql'] = cql_penalty.item()
        metrics['critic_cql_logsum'] = cql_logsumexp.item()

        return metrics

    def update_actor(self, obs, action, step):
        metrics = dict()

        policy = self.actor(obs)
        sampled_action = policy.rsample()
        log_pi = policy.log_prob(sampled_action)

        # update lagrange multiplier
        alpha_loss = -(self.log_actor_alpha *
                       (log_pi + self.target_entropy).detach()).mean()
        self.actor_alpha_opt.zero_grad()
        alpha_loss.backward()
        self.actor_alpha_opt.step()
        alpha = self.log_actor_alpha.exp().detach()

        # optimize actor
        Q1, Q2 = self.critic(obs, sampled_action)
        Q = torch.min(Q1, Q2)
        actor_loss = (alpha * log_pi - Q).mean()
        self.actor_opt.zero_grad()
        actor_loss.backward()
        self.actor_opt.step()

        metrics['actor_loss'] = actor_loss.item()
        metrics['actor_ent'] = -log_pi.mean().item()
        metrics['actor_alpha'] = alpha.item()
        metrics['actor_alpha_loss'] = alpha_loss.item()

        return metrics

    def update_mu(self, obs, action, step):
        metrics = dict()

        mu_dist = self.mu_actor(obs)
        log_probs = mu_dist.log_prob(action)

        dist = self.actor(obs)
        sampled_action = dist.rsample()
        log_pi = dist.log_prob(sampled_action)

        Q1, Q2 = self.critic(obs, action)
        V1, V2 = self.critic(obs, sampled_action)
        V = torch.min(V1, V2)
        
        advantage = 0.5*(Q1 - V) + 0.5*(Q2 - V)
        advantage = advantage * self.method_temp
        advantage = torch.clamp(advantage, min=-10, max=10)  # clip advantage to [-10, 10]
        
        if self.neg_adv:
            loss = -(log_probs * torch.exp(-advantage))
        else:
            loss = -(log_probs * torch.exp(advantage))
        
        metrics['mu_loss_mean'] = loss.mean().item()
        metrics['mu_loss_std'] = loss.std().item()
        metrics['mu_ent'] = -log_pi.mean().item()
        metrics['mu_advantage_mean'] = advantage.mean().item()
        metrics['mu_advantage_std'] = advantage.std().item()
        metrics['mu_advantage_max'] = advantage.max().item()
        metrics['mu_advantage_min'] = advantage.min().item()
        metrics['mu_V_mean'] = V.mean().item()
        metrics['mu_V_std'] = V.std().item()
        metrics['mu_V_max'] = V.max().item()
        metrics['mu_V_min'] = V.min().item()
        metrics['mu_Q_mean'] = Q1.mean().item()
        metrics['mu_Q_std'] = Q1.std().item()
        metrics['mu_Q_max'] = Q1.max().item()
        metrics['mu_Q_min'] = Q1.min().item()
        # optimize mu
        self.mu_opt.zero_grad()
        loss.mean().backward()
        self.mu_opt.step()

        return metrics


    def update(self, replay_iter, step):
        metrics = dict()

        batch = next(replay_iter)
        obs, action, reward, discount, next_obs = utils.to_torch(
            batch, self.device)

        metrics['batch_reward'] = reward.mean().item()

        # update critic
        metrics.update(
            self.update_critic(obs, action, reward, discount, next_obs, step))

        # update actor
        metrics.update(self.update_actor(obs, action, step))

        # update mu
        metrics.update(self.update_mu(obs, action, step))

        # update critic target
        utils.soft_update_params(self.critic, self.critic_target,
                                 self.critic_target_tau)

        # wandb.log(metrics, step=step)
        return metrics
