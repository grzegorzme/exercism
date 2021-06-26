def triangle_check(f):
    def wrapper(sides):
        if min(sides) <= 0:
            return False
        sides = sorted(sides)
        if sum(sides[:2]) < sides[2]:
            return False
        else:
            return f(sides)

    return wrapper


@triangle_check
def equilateral(sides):
    return len(set(sides)) == 1


@triangle_check
def isosceles(sides):
    return len(set(sides)) <= 2


@triangle_check
def scalene(sides):
    return len(set(sides)) == 3
