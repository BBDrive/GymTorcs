import gym
import numpy as np
# Gym Torcs dep.
import gym_torcs

try:
  # Instantiate the environment
  env = gym.make( "Torcs-v0")

  o ,r, done = env.reset(), 0., False
  while not done:
    action = np.tanh(np.random.randn(env.action_space.shape[0]))
    o, r, done, _ = env.step( action)

except Exception as e:
  print( e)

finally:
  env.end()
