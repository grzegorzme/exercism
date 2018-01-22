def is_palindrome(x):
    x = str(x)
    n = len(x)
    return x[:n//2+1] == x[-(n//2+1):][::-1]


def extreme_palindromes(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError('min / max invalid')
    l_min = []
    l_max = []
    v_min = None
    v_max = None
    for x in range(min_factor, max_factor + 1):
        for y in range(x, max_factor + 1):
            p = x * y
            if (v_max is None or p > v_max) and is_palindrome(str(p)):
                l_max = [(x, y)]
                v_max = p
            elif p == v_max:
                l_max.append((x, y))
            if (v_min is None or p < v_min) and is_palindrome(str(p)):
                l_min = [(x, y)]
                v_min = p
            elif p == v_min:
                l_min.append((x, y))

    return {
        'largest': (v_max, l_max),
        'smallest': (v_min, l_min)
    }


def largest_palindrome(max_factor, min_factor=0):
    result = extreme_palindromes(max_factor=max_factor, min_factor=min_factor)
    if result['largest'][0] is None:
        raise ValueError('None in range')
    return result['largest']


def smallest_palindrome(max_factor, min_factor=0):
    result = extreme_palindromes(max_factor=max_factor, min_factor=min_factor)
    if result['smallest'][0] is None:
        raise ValueError('None in range')
    return result['smallest']

