gestures = ('wink', 'double blink', 'close your eyes', 'jump',)


def handshake(code):
    n = len(gestures)
    action_mapping = list(reversed(bin(code)))[:-2]
    print(action_mapping)
    hshake = []
    for i in range(n):
        print(action_mapping[i:i+1])
        if action_mapping[i:i+1] == ['1']:
            hshake.append(gestures[i])
    if action_mapping[n:n+1] == ['1']:
        hshake = list(reversed(hshake))
    return hshake


def secret_code(actions):
    code = 0
    n = len(gestures)
    gdict = {g: 2**i for i, g in enumerate(gestures)}
    mapping = [gdict[g] for g in actions]
    if mapping != sorted(mapping):
        code += 2**n
    return code + sum(mapping)
