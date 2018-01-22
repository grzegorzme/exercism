def board(white_position, black_position):
    if (not all(0 <= x < 8 for x in list(white_position) + list(black_position))) or (white_position == black_position):
        raise ValueError('invalid positions')

    brd = [['_' for _ in range(8)] for _ in range(8)]
    brd[white_position[0]][white_position[1]] = 'W'
    brd[black_position[0]][black_position[1]] = 'B'
    print([''.join(x) for x in brd])
    return [''.join(x) for x in brd]


def can_attack(white_position, black_position):
    board(white_position=white_position, black_position=black_position)

    if white_position[0] == black_position[0] or white_position[1] == black_position[1] or \
       abs((white_position[1]-black_position[1]) / (white_position[0]-black_position[0])) == 1:
        return True
    return False
