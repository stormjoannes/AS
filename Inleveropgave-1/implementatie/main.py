from agent import Agent
from maze import Maze
from policy import Policy


def fillDict(value, sizeHorizontal=4, sizeVertical=4):
    dict = {}
    for vertical in range(sizeVertical):
        for horizontal in range(sizeHorizontal):
            coord = (vertical, horizontal)
            dict[coord] = value

    return dict


maze = Maze()
maze.grid, maze.rewards = fillDict([]), fillDict(0)
print(maze.grid)