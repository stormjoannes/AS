"""In this file we make sure everything is connected and run properly"""

from maze import Maze
from agent import Agent
from policy import Policy

policy_input = input("Policy's, 1: Monte-Carlo, 2: Temporal difference, 3: Random policy: ")
discount = float(input("What is the discount, 1 or 0.9: "))


delta_threshold = 0.01
start_position = [3, 2]

maze = Maze()
maze.position = start_position
maze.create_maze_values()

policy = Policy(maze, discount, policy_input)

agent = Agent(start_position, maze, policy, discount, delta_threshold)
agent.value_iteration()
