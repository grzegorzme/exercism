def rail_generator(n_rails):
    r = 0
    d = 1
    while True:
        yield r
        if r + 1 == n_rails:
            d = -1
        if r == 0:
            d = 1
        r += d


def fence_pattern(rails, message_size):
    pass


def encode(message, rails):
    clean_message = ''.join(message.split())
    railgen = rail_generator(rails)
    encoder = [[(r, i), c] for c, i, r in zip(clean_message, range(len(clean_message)), railgen)]
    return ''.join([x[1] for x in sorted(encoder)])


def decode(encoded_message, rails):
    railgen = rail_generator(rails)
    railpattern = sorted([next(railgen) for _ in encoded_message])
    indexpattern = [None for _ in railpattern]

    index = 0
    railgen = rail_generator(rails)
    while any(x is None for x in indexpattern):
        current_rail = next(railgen)
        for i, r in enumerate(railpattern):
            if r == current_rail and indexpattern[i] is None:
                indexpattern[i] = index
                index += 1
                break

    decoder = [[(i, r), c] for c, r, i in zip(encoded_message, railpattern, indexpattern)]
    return ''.join([x[1] for x in sorted(decoder)])
