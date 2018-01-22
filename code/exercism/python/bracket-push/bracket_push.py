def check_brackets(input_string):
    stack = []
    lbrackets = '([{'
    rbrackets = ')]}'
    for c in input_string:
        if c in lbrackets:
            stack.append(lbrackets.index(c))
        elif c in rbrackets:
            if len(stack) == 0 or stack.pop() != rbrackets.index(c):
                return False
    return stack == []
