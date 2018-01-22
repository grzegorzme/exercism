import math
from collections import Counter
from operator import mul
from functools import reduce


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def prime_factors(natural_number):
    if natural_number > 1:
        primes = gen_primes()
        p = next(primes)
        while natural_number % p != 0 and p <= math.sqrt(natural_number):
            p = next(primes)
        if p > math.sqrt(natural_number):
            return [natural_number]
        return [p] + prime_factors(natural_number // p)
    else:
        return []


def classify(number):
    if number < 1:
        raise ValueError('Invalid input')
    if number == 1:
        return 'deficient'
    pfactors = Counter(prime_factors(number))
    aliquot = reduce(mul, [(p ** (k+1) - 1) // (p-1) for p, k in pfactors.items()]) - number
    return 'perfect' if aliquot == number else \
           'abundant' if aliquot > number else \
           'deficient'
