#!/usr/bin/env python

import numpy as np
from typing import List

class Environment():
    """Simple dummy environment"""

    # The default limit to the number of time steps for the agents is 10
    def __init__(self, steps_left=10):
        self.steps_left = steps_left
        self.last_action = None

    def get_observation(self) -> List[float]:
        """
        Returns the current environment state. In this case it will be the 
        number of times each action is taken (similar to bandit problem)
        """
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        """Returns the available actions the agent can perform"""
        return [0, 1, 2]

    def is_done(self) -> bool:
        """Check if there is any time steps left"""
        return self.steps_left == 0

    # This is the central piece in the enviroment's functionality.
    # It does two things:
    # a) handles the agent's action
    # b) return the rewards (random in this example)
    def step(self, action:int) -> int:
        """"""
        if self.is_done():
            raise Exception("Game is over")

        self.last_action = action
        self.steps_left -= 1
        return np.random.randint(1, 10)


class Agent():
    """docstring for Agent."""

    def __init__(self):
        self.total_reward = 0

    # The step function allows the agent to perform the following actions
    # a) Observe the enviroment
    # b) Make a decision based on the observation
    # c) Submit the action to the environment
    # d) Get the reward from the current step
    def step(self, env):
        _ = env.get_observation()
        actions = env.get_actions()
        reward = env.step(np.random.choice(actions))
        self.total_reward += reward

if __name__ == "__main__":

    user_prompt = ("Would you like to increase the steps limit? Default limit " 
                   + "is at 10. If yes, please enter a valid number: ")

    try:
        usr_limit = int(input(user_prompt))
    except Exception as e:
        print('\nYou have opted for default limit')
        env = Environment()
    else:
        env = Environment(usr_limit)

    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print('\n----')
    print("Total reward accumulated: {:,}".format(agent.total_reward))
