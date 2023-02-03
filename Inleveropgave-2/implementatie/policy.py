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

        opt_1 = self.maze.stepper(position, 0)  # up
        opt_2 = self.maze.stepper(position, 1)  # down
        opt_3 = self.maze.stepper(position, 2)  # right
        opt_4 = self.maze.stepper(position, 3)  # left
        options = [opt_1, opt_2, opt_3, opt_4]

        if self.policy_input == '1':
            # Get all 4 surrounding values calculated, pick the max value, aka the optimal move.
            new_value = self.monte_carlo(options, iteration)

        elif self.policy_input == '2':
            self.temporal_difference(options, iteration)

        elif self.policy_input == '3':
            new_value = self.random_policy(options, iteration)

        return new_value

    def monte_carlo(self, options, iteration):
        new_value = max(self.maze.rewards[options[0]] + (self.discount * self.maze.grid[options[0]][iteration]),
                        self.maze.rewards[options[1]] + (self.discount * self.maze.grid[options[1]][iteration]),
                        self.maze.rewards[options[2]] + (self.discount * self.maze.grid[options[2]][iteration]),
                        self.maze.rewards[options[3]] + (self.discount * self.maze.grid[options[3]][iteration]))
        return new_value

    def temporal_difference(self, options, iteration):
        new_value = 5

        return new_value

    def random_policy(self, options, iteration):
        random_choice = random.choice(options)
        new_value = self.maze.rewards[random_choice] + (self.discount * self.maze.grid[random_choice][iteration])

        return new_value
