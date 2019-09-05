import random

class Environment:
    """docstring for Environment."""

    # The default limit to the number of time steps for the agents is 10
    def __init__(self, steps_left=10):
        self.steps_left = steps_left

    # Returns the current environment state
    def get_observation(self):
        return [0.0, 0.0, 0.0]

    # This method allows the agent to query the set of actions it can execute
    # In this mini-example, the agent have only two possible actions at
    # any time-step.
    def get_actions(self):
        return [0, 1]

    # Check if there is any time steps left
    def is_done(self):
        return self.steps_left == 0

    # This is the central piece in the enviroment's functionality.
    # It does two things:
    # a) handles the agent's action
    # b) return the rewards (random in this example)
    def action(self, action):
        if self.is_done():
            raise Exception("Game is over")

        self.steps_left -= 1
        return random.randint(1, 10)

class Agent(object):
    """docstring for Agent."""

    def __init__(self):
        self.total_reward = 0

    # The step function allows the agent to perform the following actions
    # a) Observe the enviroment
    # b) Make a decision based on the observation
    # c) Submit the action to the environment
    # d) Get the reward from the current step
    def step(self, env):
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward

if __name__ == "__main__":

    print('Would you like to increase the steps limit? Default limit is at 10.')
    print('If yes, please enter a valid number')

    try:
        usr_limit = int(input('--> '))
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
