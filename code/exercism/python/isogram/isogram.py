def is_isogram(string):
    return len([a for a in string.lower() if a not in {' ', '-'}]) == len({a for a in string.lower() if a not in {' ', '-'}})
