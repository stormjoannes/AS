"""In this file we define our agent class"""
from maze import Maze
from policy import Policy


class Agent:
    """
    agent
    """
    actions = {"forward": 0, "backward": 1, "right": 2, "left": 3}

    def __init__(self, pos, maze: Maze, policy: Policy, discount):
        self.pos = pos
        self.maze = Maze
        self.policy = Policy
        self.discount = discount

    def value_function(self):
        """
        Value function
        """
        pass

    def choose_action(self, policy, state):
        """
        Actions choser
        """
        pass
    
    def value_iteration(self):
        """
        Value iteration.
        """
        pass
