def sum_of_multiples(limit, multiples):
    return sum(set([y for x in [range(x, limit, x) for x in multiples] for y in x]))
