"""In this file we define our agent class"""
from maze import Maze
from policy import Policy


class Agent:
    """
    agent
    """
    actions = {"forward": 0, "backward": 1, "right": 2, "left": 3}

    def __init__(self, position, maze: Maze, policy: Policy, discount, delta_treshold):
        self.position = position
        self.maze = Maze
        self.policy = Policy
        self.discount = discount
        self.delta_treshold = delta_treshold

    def stepper(self):
        """
        """
        movement = self.choose_action(self.position)
        self.position = self.maze.stepper(self.position, movement)

    def value_iteration(self):
        """
        Value iteration.
        """
        iteration = 0
        while delta >= self.delta_treshold:
            iteration += 1
            for pos in self.maze.grid:
                if pos not in self.maze.terminal_states:


        pass

    def value_function(self):
        """
        Value function
        """
        pass

    def choose_action(self, state):
        """
        Actions choser
        """
        return self.policy.select_action(state)
