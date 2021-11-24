"""In this file we define our agent class"""
from maze import Maze
from policy import Policy


class Agent:
    """
    agent
    """
    actions = {"forward": 0, "backward": 1, "right": 2, "left": 3}

    def __init__(self, pos, maze: Maze, policy: Policy):
        self.pos = pos
        self.maze = Maze
        self.policy = Policy

    def choose_action(self, policy, state):
        pass
    
    def value_iteration(self):
        pass
