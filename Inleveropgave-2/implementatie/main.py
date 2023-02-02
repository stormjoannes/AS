"""In this file we make sure everything is connected and run properly"""

from maze import Maze
from agent import Agent
from policy import Policy

policy_input = input("Type 1 for Monte-Carlo, type 2 for random policy: ")
discount = float(input("What is the discount, 1 or 0.9: "))


delta_treshold = 0.01
start_position = [3, 2]

maze = Maze()
maze.position = start_position
maze.create_maze_values()

policy = Policy(maze, discount, policy_input)

agent = Agent(start_position, maze, policy, discount, delta_treshold)
agent.value_iteration()
