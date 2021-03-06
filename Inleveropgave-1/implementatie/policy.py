"""In this file we define our policy class"""
import random


class Policy:
    
    def __init__(self):
        """
        Defines the values of class Policy.
        """
        self.policy = "random"

    def select_action(self):
        """
        Deciding which action will be chosen, Beginning with a random policy.
        """
        return random.choice(0, 1, 2, 3)
