"""State dataclass"""
from dataclasses import dataclass

@dataclass
class State:
    x = 0
    y = 0
    reward = 0
    values = []
    terminating_state = False
