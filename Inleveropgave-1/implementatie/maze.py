"""In this file we define our maze class"""


class Maze:
    """
    hi
    """
    
    def __init__(self):
        self.position = []
        self.grid = []
        self.rewards = dict
        self.grid = dict
        self.terminal_states = list
        self.actions = {0: [-1, 0], 1: [1, 0], 2: [0, 1], 3: [0, -1]}


    def stepper(self, currentState, action):
        movement = self.actions[action]
        new_position = [self.position[0] + movement[0], self.position[1] + movement[0]]
        return nextState


    def fillDict(self, value, sizeHorizontal=4, sizeVertical=4):
        """
        Filling a dictionary with coördinates.
        """
        index = 0
        dict = {}
        for vertical in range(sizeVertical):
            for horizontal in range(sizeHorizontal):
                coord = (vertical, horizontal)
                dict[coord] = value[index]
                index += 1

        return dict


    def create_maze_values(self):
        values = [0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0]

        rewards = [-1, -1, -1, 40,
                   -1, -1, -10, -10,
                   -1, -1, -1, -1,
                   10, -2, -1, -1]

        self.terminal_states = [[0, 3], [3, 0]]

        self.grid, self.rewards = self.fillDict(values), self.fillDict(rewards)


