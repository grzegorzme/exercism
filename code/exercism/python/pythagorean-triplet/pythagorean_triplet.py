import numpy as np
import math


def primitive_triplets(number_in_triplet):
    if number_in_triplet == 5:
        raise ValueError('not sure why this error is necessary - function should return {(3, 4, 5)}')
    # a = (m ^ 2 - n ^ 2), b = 2 * m * n and c = (m ^ 2 + n ^ 2)
    triplets = []
    for n in range(1, int(number_in_triplet/2)+1):
        for m in range(n+1, int(number_in_triplet/2)+1):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if number_in_triplet in (a, b, c) and math.gcd(a, b) == math.gcd(b, c) == math.gcd(c, a) == 1:
                triplets.append(tuple(sorted((a, b, c))))
    return set(triplets)


def triplets_in_range(range_start, range_end):
    triplets = []
    for a in range(range_start, range_end):
        for b in range(a+1, range_end+1):
            c = int(np.sqrt(a**2 + b**2))
            if a**2 + b**2 == c**2 and all([range_start <= x <= range_end for x in (a, b, c)]):
                triplets.append((a, b, c))
    return set(triplets)


def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2
