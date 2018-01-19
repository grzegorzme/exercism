import numpy as np


class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(x) for x in row.split()] for row in matrix_string.split('\n')]
        self.rows = self.matrix
        self.columns = np.array(self.matrix).T.tolist()
