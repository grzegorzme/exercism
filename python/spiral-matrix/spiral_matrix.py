def spiral_matrix(size):
    if size == 0:
        return list()

    directions = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}

    prev = (0, 0)
    coordinates = {(0, 0): 1}
    d = (0, 1)

    for i in range(1, size ** 2):
        for _ in range(4):
            candidate = (prev[0] + d[0], prev[1] + d[1])
            if (
                (0 <= candidate[0] < size)
                and (0 <= candidate[1] < size)
                and (candidate not in coordinates)
            ):
                coordinates[candidate] = i + 1
                prev = candidate
                break
            d = directions[d]

    return [[coordinates[x, y] for y in range(size)] for x in range(size)]
