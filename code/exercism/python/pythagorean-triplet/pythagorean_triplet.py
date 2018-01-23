import math


def divisor_pair_gen(n, include_trivial=False, coprime=False):
    start = 1 if include_trivial else 2
    end = int(math.sqrt(n)) + 1
    for i in range(start, end):
        if n % i == 0 and (math.gcd(i, n // i) == 1 if coprime else True):
            print(i, n // i)
            yield (i, n // i)
    raise StopIteration


def primitive_triplets(number_in_triplet):
    # a = (m ^ 2 - n ^ 2), b = 2 * m * n and c = (m ^ 2 + n ^ 2)
    if number_in_triplet % 4 != 0:
        raise ValueError('number_in_triplet must be divisable by 4, because either m or n is even')
    triplets = []
    for n, m in divisor_pair_gen(number_in_triplet // 2, include_trivial=True, coprime=True):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        triplets.append(tuple(sorted((a, b, c))))
    return set(triplets)


def triplets_in_range(range_start, range_end):
    triplets = []
    for a in range(range_start, range_end):
        for b in range(a+1, range_end+1):
            c = int(math.sqrt(a**2 + b**2))
            if a**2 + b**2 == c**2 and all([range_start <= x <= range_end for x in (a, b, c)]):
                triplets.append((a, b, c))
    return set(triplets)


def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2
