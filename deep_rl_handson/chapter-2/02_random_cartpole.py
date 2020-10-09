#!/usr/bin/env python

import gym

if __name__ == "__main__":
    # Create a CartPole environment
    env = gym.make('CartPole-v0')

    # Initialize variables
    total_reward = 0
    total_steps = 0

    # Reset the environment before starting it
    obs = env.reset()

    while True:
        # Perform a random action
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        total_steps += 1

        # Check if game is finished
        if done:
            break

print(f"Episode done in {total_steps} steps, total reward {total_reward:,.2f}")
