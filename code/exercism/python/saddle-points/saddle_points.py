import numpy as np
import itertools


def saddle_points(matrix):
    if matrix == list():
        return set()
    mx = max(len(u) for u in matrix)
    if any(len(x) != mx for x in matrix):
        raise ValueError('not a matrix')
    m = np.matrix(matrix)
    mb = (m == m.min(0)) & (m == m.max(1))
    return set([(x, y) for x, y in itertools.product(range(m.shape[0]), range(m.shape[1])) if mb[x, y]])
