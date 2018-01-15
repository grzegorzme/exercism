def flatten(iterable):
    result = []
    for x in iterable:
        if type(x) in (list, tuple):
            result += flatten(x)
        else:
            result.append(x)
    return [x for x in result if x is not None]
