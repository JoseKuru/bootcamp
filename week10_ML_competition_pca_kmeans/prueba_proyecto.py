import time
import gym

env = gym.make('SpaceInvaders-v0')
print(env.action_space)
print(env.observation_space.sample().shape)