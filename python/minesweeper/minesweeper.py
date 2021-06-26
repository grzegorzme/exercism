def index_gen(coord, shape):
    neighbors_ = (-1, 0, 1)
    for dx in neighbors_:
        for dy in neighbors_:
            if not (dx == 0 and dy == 0):
                new_x, new_y = coord[0] + dx, coord[1] + dy
                if 0 <= new_x < shape[0] and 0 <= new_y < shape[1]:
                    yield (new_x, new_y)


def annotate(input_board_array):
    if input_board_array == list():
        return []
    # check for invalid characters
    if not all(c in " *" for c in "".join(input_board_array)):
        raise ValueError("invalid value encountered")
    if min(len(x) for x in input_board_array) != max(len(x) for x in input_board_array):
        raise ValueError("invalid board shape")

    shape = (len(input_board_array), len(input_board_array[0]))

    output_board_array = [[0 if y == " " else y for y in x] for x in input_board_array]

    print(output_board_array)

    for x in range(shape[0]):
        for y in range(shape[1]):
            if output_board_array[x][y] == "*":
                print(x, y)
                for x1, y1 in index_gen((x, y), shape):
                    if output_board_array[x1][y1] != "*":
                        output_board_array[x1][y1] += 1

    return ["".join(str(y) if y != 0 else " " for y in x) for x in output_board_array]
