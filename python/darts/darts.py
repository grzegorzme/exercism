def score(x, y):
    d2 = x * x + y * y
    if d2 <= 1:
        return 10
    if d2 <= 25:
        return 5
    if d2 <= 100:
        return 1
    return 0
