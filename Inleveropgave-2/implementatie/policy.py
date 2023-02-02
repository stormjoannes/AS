"""In this file we define our policy class"""
import random


class Policy:
    
    def __init__(self, maze, discount, policy_input):
        """
        Defines the values of class Policy.
        """
        self.maze = maze
        self.discount = discount
        self.policy_input = policy_input
        self.policy = "random"

    def select_action(self, position, iteration):
        """
        Deciding which action will be chosen, Beginning with a random policy.
        """
        opt_1 = self.maze.stepper(position, 0) #up
        opt_2 = self.maze.stepper(position, 1) #down
        opt_3 = self.maze.stepper(position, 2) #right
        opt_4 = self.maze.stepper(position, 3) #left

        if self.policy_input == '1':
            # Get all 4 surrounding values calculated, pick the max value, aka the optimal move.
            new_value = max(self.maze.rewards[opt_1] + (self.discount * self.maze.grid[opt_1][iteration]),
                            self.maze.rewards[opt_2] + (self.discount * self.maze.grid[opt_2][iteration]),
                            self.maze.rewards[opt_3] + (self.discount * self.maze.grid[opt_3][iteration]),
                            self.maze.rewards[opt_4] + (self.discount * self.maze.grid[opt_4][iteration]))

        elif self.policy_input == '2':
            random_choice = random.choice([opt_1, opt_2, opt_3, opt_4])
            new_value = self.maze.rewards[random_choice] + (self.discount * self.maze.grid[random_choice][iteration])

        return new_value
