#!usr/bin/env python

import numpy as np

class EpsilonGreedy():
    """"""
    def __init__(self, n_arms, epsilon=0.1):
        """
        Initialize the object
        
        Parameters
        ----------
        n_arms : int
            Number of available arms/actions

        epsilon : float, default 0.1
            The percentage of times the agent will do exploration
        """
        self.n_arms = n_arms
        self.epsilon = epsilon
        self.reset()
    
    def reset(self):
        """Reset the arm counts and values"""
        self.arm_counts = [0 for col in range(self.n_arms)]
        self.q_values = [0.0 for col in range(self.n_arms)]

    def argmax(self) -> int:
        """Return the index of the highest q_values. Random if ties"""
        # Find the highest value
        max_val = np.max(self.q_values)

        # Filter the list 
        index_list = [i for i, j in enumerate(self.q_values) if j == max_val]

        # In the event that more than one exist, select randomly
        max_index = int(np.random.choice(index_list))

        return max_index
    
    def select_arm(self) -> int:
        """Exploit if random value higher than epsilon, else explore randomly"""
        rng_val = np.random.default_rng().random(size=1)
        if rng_val >= self.epsilon:
            current_action = self.argmax()
            return current_action

        return np.random.randint(len(self.q_values))

    def update(self, chosen_arm, reward):
        """Update the q_values and the arm_counts"""
        self.arm_counts[chosen_arm] += 1

        # Update the q_values using the incremental update rule formula
        step_size = 1/(self.arm_counts[chosen_arm])

        self.q_values[chosen_arm] += (step_size
                                      *(reward-self.q_values[chosen_arm]))
    
    

        