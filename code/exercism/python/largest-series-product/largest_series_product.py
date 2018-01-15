from functools import reduce


def largest_product(series, size):
    if size < 0:
        raise ValueError('Error')
    if size == 0:
        return 1
    return max([reduce(lambda x, y: x*y, [int(x) for x in series[n:n+size]]) for n in range(0, len(series)-size+1)])
