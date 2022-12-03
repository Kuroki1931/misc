from datetime import datetime
import functools
import os

import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt
import brax

from brax import envs
from brax import jumpy as jp
from brax.training import ppo, sac
from brax.io import html
from brax.io import model

import os
os.environ["CUDA_VISIBLE_DEVICES"]="0" 
local_device_count = jax.local_device_count()
print('local_device_count', local_device_count)
assert local_device_count == 1, f'your devide is {local_device_count} too much device'


env_name = "grasp"  # @param ['ant', 'humanoid', 'fetch', 'grasp', 'halfcheetah', 'ur5e', 'reacher', 'walker2d']
env_fn = envs.create_fn(env_name=env_name)
env = env_fn()
state = env.reset(rng=jp.random_prngkey(seed=0))
html.save_html('test.html', env.sys, [state.qp])

train_fn = {
  'grasp': functools.partial(
      ppo.train, num_timesteps = 600_000_000, log_frequency = 10,
      reward_scaling = 10, episode_length = 1000, normalize_observations = True,
      action_repeat = 1, unroll_length = 20, num_minibatches = 32,
      num_update_epochs = 2, discounting = 0.99, learning_rate = 3e-4,
      entropy_cost = 0.001, num_envs = 2048, batch_size = 256
  ),
}[env_name]
max_y = {'grasp': 1000}[env_name]
min_y = {'reacher': -100}.get(env_name, 0)
xdata = []
ydata = []
times = [datetime.now()]

output_dir = os.path.join(
    f'results/{env_name}/{datetime.now().strftime("%Y%m%d_%H%M%S")}')
os.makedirs(output_dir, exist_ok=True)


def progress(num_steps, metrics):
  times.append(datetime.now())
  xdata.append(num_steps)
  ydata.append(metrics['eval/episode_reward'])
  plt.xlim([0, train_fn.keywords['num_timesteps']])
  plt.ylim([min_y, max_y])
  plt.xlabel('# environment steps')
  plt.ylabel('reward per episode')
  plt.plot(xdata, ydata)
  plt.savefig(f'{output_dir}/reward.png', bbox_inches='tight')

inference_fn, params, _ = train_fn(environment_fn=env_fn, progress_fn=progress)

print(f'time to jit: {times[1] - times[0]}')
print(f'time to train: {times[-1] - times[1]}')

jit_env_reset = jax.jit(env.reset)
jit_env_step = jax.jit(env.step)
jit_inference_fn = jax.jit(inference_fn)

rollout = []
rng = jax.random.PRNGKey(seed=0)
state = jit_env_reset(rng=rng)
while not state.done:
  rollout.append(state)
  act_rng, rng = jax.random.split(rng)
  act = jit_inference_fn(params, state.obs, act_rng)
  state = jit_env_step(state, act)

html.save_html(f'{output_dir}/ppo.html', env.sys, [s.qp for s in rollout])