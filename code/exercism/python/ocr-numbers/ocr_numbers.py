import numpy as np

default_width = 3
default_height = 4

shape_dict = {
    ((' ', ' ', ' '),
     (' ', ' ', '|'),
     (' ', ' ', '|'),
     (' ', ' ', ' ')): '1',
    ((' ', '_', ' '),
     (' ', '_', '|'),
     ('|', '_', ' '),
     (' ', ' ', ' ')): '2',
    ((' ', '_', ' '),
     (' ', '_', '|'),
     (' ', '_', '|'),
     (' ', ' ', ' ')): '3',
    ((' ', ' ', ' '),
     ('|', '_', '|'),
     (' ', ' ', '|'),
     (' ', ' ', ' ')): '4',
    ((' ', '_', ' '),
     ('|', '_', ' '),
     (' ', '_', '|'),
     (' ', ' ', ' ')): '5',
    ((' ', '_', ' '),
     ('|', '_', ' '),
     ('|', '_', '|'),
     (' ', ' ', ' ')): '6',
    ((' ', '_', ' '),
     (' ', ' ', '|'),
     (' ', ' ', '|'),
     (' ', ' ', ' ')): '7',
    ((' ', '_', ' '),
     ('|', '_', '|'),
     ('|', '_', '|'),
     (' ', ' ', ' ')): '8',
    ((' ', '_', ' '),
     ('|', '_', '|'),
     (' ', '_', '|'),
     (' ', ' ', ' ')): '9',
    ((' ', '_', ' '),
     ('|', ' ', '|'),
     ('|', '_', '|'),
     (' ', ' ', ' ')): '0',


}


def validate(input_grid, height=default_height, width=default_width):
    if len(input_grid) % height != 0:
        raise ValueError('invalid height')
    mx = max(len(x) for x in input_grid)
    mn = min(len(x) for x in input_grid)
    if mx != mn or mx % width != 0 or mn % width != 0:
        raise ValueError('invalid weight')


def transform_input(input_grid):
    mat = [list(x) for x in input_grid]
    return np.array(mat, dtype=np.str)


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
