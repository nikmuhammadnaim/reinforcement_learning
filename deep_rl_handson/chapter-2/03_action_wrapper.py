#!/usr/bin/env python
import gym
from typing import TypeVar
import random

Action = TypeVar('Action')

class RandomActionWrapper(gym.ActionWrapper):
    """docstring for RandomActionWrapper."""

    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        self.epsilon = epsilon

    def action(self, action:Action) -> Action:
        if random.random() < self.epsilon:
            print('Re-random given action')
            return self.env.action_space.sample()
        return action

if __name__ == '__main__':
    env = RandomActionWrapper(gym.make('CartPole-v0'))

    obs = env.reset()
    total_reward = 0.0

    while True:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    print('Reward received: {}'.format(total_reward))
