"""In this file we will iterate over values"""
from maze import Maze
from policy import Policy


class Agent:

    def __init__(self, position, Maze, Policy, discount, delta_treshold):
        self.position = position
        self.maze = Maze
        self.policy = Policy
        self.discount = discount
        self.delta_treshold = delta_treshold
        self.actions = {0: [-1, 0], 1: [1, 0], 2: [0, 1], 3: [0, -1]}

    def value_iteration(self):
        """
        Iterating over the maze grid and calculate each value for each iteration.
        """
        # Make sure the first time iteration it will always go into the while loop.
        delta = self.delta_treshold + 1
        iteration = 0
        while delta >= self.delta_treshold:
            # Set delta low so that first loop delta will always be overwritten.
            delta = -1
            for position in self.maze.grid:
                # Check if position isn't an terminal state.
                if position not in self.maze.terminal_states:
                    # Gets the coords of the states surrounding the current position.
                    up = self.maze.stepper(position, 0)
                    down = self.maze.stepper(position, 1)
                    right = self.maze.stepper(position, 2)
                    left = self.maze.stepper(position, 3)

                    # Get all 4 surrounding values calculated, pick the max from these values.
                    new_value = max(self.maze.rewards[up] + (self.discount * self.maze.grid[up][iteration]),
                                    self.maze.rewards[down] + (self.discount * self.maze.grid[down][iteration]),
                                    self.maze.rewards[right] + (self.discount * self.maze.grid[right][iteration]),
                                    self.maze.rewards[left] + (self.discount * self.maze.grid[left][iteration]))

                    self.maze.grid[position].append(new_value)
                    new_delta = abs(self.maze.grid[position][iteration] - new_value)
                    delta = new_delta if new_delta > delta else delta
                else:
                    # If state is terminal state, new value is always zero.
                    self.maze.grid[position].append(0)

            self.print_iteration(iteration)
            iteration += 1

    def choose_action(self):
        """
        Choose where the next step will be.
        """
        return self.policy.select_action()

    def print_iteration(self, iteration):
        """
        Quick hardcoded print to show values for each iteration.
        """
        values = []
        for coord in self.maze.grid:
            values.append(self.maze.grid[coord][iteration])

        print("Iteration: ", iteration)
        print(values[0: 4])
        print(values[4: 8])
        print(values[8: 12])
        print(values[12: 16], "\n")
