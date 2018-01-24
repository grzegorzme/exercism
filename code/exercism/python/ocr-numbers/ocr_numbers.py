import numpy as np

default_width = 3
default_height = 4

shape_dict = {
    ((0, 0, 0),
     (0, 0, 1),
     (0, 0, 1),
     (0, 0, 0)): '1',
    ((0, 2, 0),
     (0, 2, 1),
     (1, 2, 0),
     (0, 0, 0)): '2',
    ((0, 2, 0),
     (0, 2, 1),
     (0, 2, 1),
     (0, 0, 0)): '3',
    ((0, 0, 0),
     (1, 2, 1),
     (0, 0, 1),
     (0, 0, 0)): '4',
    ((0, 2, 0),
     (1, 2, 0),
     (0, 2, 1),
     (0, 0, 0)): '5',
    ((0, 2, 0),
     (1, 2, 0),
     (1, 2, 1),
     (0, 0, 0)): '6',
    ((0, 2, 0),
     (0, 0, 1),
     (0, 0, 1),
     (0, 0, 0)): '7',
    ((0, 2, 0),
     (1, 2, 1),
     (1, 2, 1),
     (0, 0, 0)): '8',
    ((0, 2, 0),
     (1, 2, 1),
     (0, 2, 1),
     (0, 0, 0)): '9',
    ((0, 2, 0),
     (1, 0, 1),
     (1, 2, 1),
     (0, 0, 0)): '0',


}


def validate(input_grid, height=default_height, width=default_width):
    if len(input_grid) % height != 0:
        raise ValueError('invalid height')
    mx = max(len(x) for x in input_grid)
    mn = min(len(x) for x in input_grid)
    if mx != mn or mx % width != 0 or mn % width != 0:
        raise ValueError('invalid weight')


def transform_input(input_grid):
    mat = [[0 if xx == ' ' else
            1 if xx == '|' else
            2 if xx == '_' else
            100 for xx in x] for x in input_grid]
    return np.array(mat)


def convert(input_grid):
    validate(input_grid)
    grid = transform_input(input_grid)
    output = []
    for i in range(0, grid.shape[0], default_height):
        if i > 0:
            output.append(',')
        for j in range(0, grid.shape[1], default_width):
            shp = tuple(map(tuple, grid[i:i+default_height, j:j+default_width]))
            output.append(shape_dict.get(shp, '?'))
    return ''.join(output)
