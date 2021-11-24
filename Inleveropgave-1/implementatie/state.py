"""State dataclass"""
from dataclasses import dataclass

@dataclass
class State:
    xy_coord = [0, 0]
    reward = 0
    finished = False
