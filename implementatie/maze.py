currentPos = [0, 0]

def stepper(x, y, reward, boolean):


def fillDict(value, sizeHorizontal = 4, sizeVertical = 4):
    dict = {}
    for vertical in range(sizeVertical):
        for horizontal in range(sizeHorizontal):
            coord = (vertical, horizontal)
            dict[coord] = value


    return dict

grid = fillDict([])
rewards = fillDict(0)
Actions = {"forward": 0, "backward": 1, "right": 2, "left": 3}