def square_of_sum(n):
    return (n*(n+1) / 2) ** 2


def sum_of_squares(n):
    return sum(n**2 for n in range(1, n+1))


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
