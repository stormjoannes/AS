"""In this file we make sure everything is connected and run properly"""

from agent import Agent
from maze import Maze
from agent import Agent
from policy import Policy


def fillDict(value, sizeHorizontal=4, sizeVertical=4):
    index = 0
    dict = {}
    for vertical in range(sizeVertical):
        for horizontal in range(sizeHorizontal):
            coord = (vertical, horizontal)
            dict[coord] = value[index]
            index += 1

    return dict


delta = 0.1
start_position = [3, 2]
values = [0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0,
          0, 0, 0, 0]
rewards = [-1, -1, -1, 40,
           -1, -1, -10, -10,
           -1, -1, -1, -1,
           10, -2, -1, -1]

maze = Maze()
maze.grid, maze.rewards = fillDict(values), fillDict(rewards)
agent = Agent(start_position)
print(maze.rewards)
