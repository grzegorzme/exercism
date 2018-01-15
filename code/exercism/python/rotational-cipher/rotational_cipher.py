import string


def rotate(text, key):
    cipher = []
    for c in text:
        if c in string.ascii_lowercase:
            cipher.append(string.ascii_lowercase[(string.ascii_lowercase.index(c) + key) % 26])
        elif c in string.ascii_uppercase:
            cipher.append(string.ascii_uppercase[(string.ascii_uppercase.index(c) + key) % 26])
        else:
            cipher.append(c)
    return ''.join(cipher)
