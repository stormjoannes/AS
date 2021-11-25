"""In this file we make sure everything is connected and run properly"""

from agent import Agent
from maze import Maze
from agent import Agent
from policy import Policy


delta = 0.1
discount = 1
start_position = [3, 2]

maze = Maze()
maze.position = start_position
maze.create_maze_values()

policy = Policy()

agent = Agent(start_position, maze, policy, discount)
print(maze.rewards)
