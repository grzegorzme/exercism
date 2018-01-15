import numpy as np

# Globals for the bearings
# Change the values as you see fit

EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)

rotation_90 = np.array([[0, 1], [-1, 0]], dtype=np.int)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def advance(self):
        self.coordinates = tuple(np.array(self.coordinates, dtype=np.int) + np.array(self.bearing, dtype=np.int))

    def turn_right(self):
        self.bearing = tuple(np.matmul(rotation_90, np.array(self.bearing, dtype=np.int)))

    def turn_left(self):
        self.bearing = tuple(-np.matmul(rotation_90, np.array(self.bearing, dtype=np.int)))

    def simulate(self, instructions):
        for ins in instructions:
            if ins == 'A':
                self.advance()
            elif ins == 'R':
                self.turn_right()
            elif ins == 'L':
                self.turn_left()
            else:
                raise ValueError('Unexpected instruction: {}'.format(ins))
