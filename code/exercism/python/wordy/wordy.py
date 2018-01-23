import ast


def op(op_, x, y):
    if op_ == '+':
        return x + y
    elif op_ == '-':
        return x - y
    elif op_ == '*':
        return x * y
    elif op_ == '/':
        return x / y


def isnumber(x):
    try:
        ast.literal_eval(x)
    except:
        return False
    return True


op_dict = {
    'plus': '+',
    'minus': '-',
    'multiplied by': '*',
    'divided by': '/',
}


def calculate(question):
    q = question.lower().replace('?', '')
    for k, v in op_dict.items():
        q = q.replace(' ' + k + ' ', ' ' + v + ' ')
    q = q.split()
    q = [w for w in q if isnumber(w) or w in op_dict.values()]
    q = list(map(lambda x: ast.literal_eval(x) if isnumber(x) else x, q))
    # evaluation
    print(q)
    if len(q) < 3:
        raise ValueError('something is not right')
    if not all([(type(w) == str) if (i % 2 == 1) else True for i, w in enumerate(q)]):
        raise ValueError('something is not right')
    while len(q) > 2:
        q = [op(q[1], q[0], q[2])] + q[3:]
    return q[0]
