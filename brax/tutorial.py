from datetime import datetime
import functools
import os
import pprint
import jax
import jax.numpy as jnp
from IPython.display import HTML, clear_output
import matplotlib.pyplot as plt


import brax
from brax.io import html
from brax.experimental import biggym
from brax.experimental.composer import composer
from brax.experimental.composer.training import mappo
from brax.experimental.braxlines import experiments
from brax.experimental.braxlines.common import evaluators
from brax.experimental.braxlines.common import logger_utils
from brax.experimental.braxlines.training import ppo

import os
os.environ["CUDA_VISIBLE_DEVICES"]="0" 
local_device_count = jax.local_device_count()
print('local_device_count', local_device_count)
assert local_device_count == 1, f'your devide is {local_device_count} too much device'

def show_env(env):
  jit_env_reset = jax.jit(env.reset)
  state = jit_env_reset(rng=jax.random.PRNGKey(seed=0))
  clear_output(wait=True)
  html.save_html('test.html', env.sys, [state.qp])


registry_name = 'particle'
register_all = True

if register_all:
  biggym.register_all(verbose=True)
  pprint.pprint(biggym.ENVS_BY_TRACKS)
env_names, comp_names, task_env_names, _ = biggym.register(registry_name)
print(f'env_names: {env_names}') # particle_envs Manipulationを保存 in ENV_DESCS
print(f'comp_names: {comp_names}') # particle_particle components呼ぶよう antの構造が入っている in COMPONENT_MAPPING
print(f'task_env_names: {task_env_names}') # block__particle__particle task comp_name格納 in ENV_DESCS


#@title Specify an environment
env_name = 'particle__manipulation' # @param {type: 'string'}
output_path = '' # @param {type: 'string'}
show_params = True # @param {'type':'boolean'}

if output_path:
  output_path = f'{output_path}/{datetime.now().strftime("%Y%m%d")}' 
  output_path = f'{output_path}/{env_name}'
  print(f'Saving outputs to {output_path}')

if show_params:
  supported_params, support_kwargs = biggym.inspect_env(env_name=env_name) # ENV_DESCSにしまったenv_nmaeと紐づけられたtask_nameの引数が見える
  # task
  # def block(component: str,
  #        opponent: str = 'ant',
  #        opponent_params: Dict[str, Any] = None,
  #        **component_params):
  print(f'supported_params for "{env_name}" =')
  pprint.pprint(supported_params)
  print(f'support variable-length kwargs? (i.e. **kwargs): {support_kwargs}')


#@title Create a custom env

env_params =  {'num_legs': 8}# @param{'type': 'raw'}
mode = 'viewer'# @param ['print_step', 'print_obs', 'print_sys', 'viewer']
ignore_kwargs = True # @param {'type':'boolean'}

# check supported params -> パラメータの確認　support_paramsに含まれているか。
env_params = env_params or {}
biggym.assert_env_params(env_name, env_params, ignore_kwargs) # 変更しようとしているparamがenv_nameと紐づく環境の引数として扱われているか確認

# create env
env_fn = composer.create_fn(env_name=env_name, **env_params)
# env_fn = biggym.create_fn(env_name=env_name, **env_params)
env = env_fn()
state = env.reset(rng=jax.random.PRNGKey(seed=0))
rollout = []
for i in range(1):
  # wiggle sinusoidally with a phase shift per actuator
  action = jnp.sin(i * jnp.pi / 15 + jnp.arange(0, env.action_size) * jnp.pi)
  state = env.step(state, action)
  rollout.append(state)
html.save_html('test.html', env.sys, [s.qp for s in rollout])


#@title Training the custom env
num_timesteps_multiplier =   2# @param {type: 'number'}
seed = 0 # @param{type: 'integer'}
skip_training = False # @param {type: 'boolean'}

log_path = output_path
if log_path:
  log_path = f'{log_path}/training_curves.csv'
tab = logger_utils.Tabulator(output_path=log_path,
    append=False)

# PPOで学習
ppo_lib = mappo if biggym.is_multiagent(env) else ppo
ppo_params = experiments.defaults.get_ppo_params(
    'ant', num_timesteps_multiplier)
train_fn = functools.partial(ppo_lib.train, **ppo_params)

times = [datetime.now()]
plotpatterns = ['eval/episode_reward', 'eval/episode_score']

progress, _, _, _ = experiments.get_progress_fn(
    plotpatterns, times, tab=tab, max_ncols=5,
    xlim=[0, train_fn.keywords['num_timesteps']],
    pre_plot_fn = lambda : clear_output(wait=True),
    post_plot_fn = plt.show)

if skip_training:
  action_size = (env.group_action_shapes if 
    biggym.is_multiagent(env) else env.action_size)
  params, inference_fn = ppo_lib.make_params_and_inference_fn(
    env.observation_size, action_size,
    normalize_observations=True)
  inference_fn = jax.jit(inference_fn)
else:
  inference_fn, params, _ = train_fn(
    environment_fn=env_fn, seed=seed,
    extra_step_kwargs=False, progress_fn=progress)
  print(f'time to jit: {times[1] - times[0]}')
  print(f'time to train: {times[-1] - times[1]}')
  print(f'Saved logs to {log_path}')


#@title Visualizing a trajectory of the learned inference function
eval_seed = 0  # @param {'type': 'integer'}
batch_size =  0# @param {type: 'integer'}

env, states = evaluators.visualize_env(
    env_fn=env_fn, inference_fn=inference_fn,
    params=params, batch_size=batch_size,
    seed = eval_seed, output_path=output_path,
    verbose=True,
)
html.save_html('ppo.html', env.sys, [state.qp for state in states])
#@title Plot information of the trajectory
experiments.plot_states(states[1:], max_ncols=5)
plt.show()

