import string


def code_single(c):
    if c in '0123456789':
        return c
    if c in string.ascii_letters:
        return list(reversed(string.ascii_lowercase))[string.ascii_lowercase.index(c.lower())]
    return ''


def encode(plain_text):
    cipher = [c for c in [code_single(c) for c in plain_text] if c]
    return ' '.join([''.join(cipher[0+i:5+i]) for i in range(0, len(cipher), 5)])


def decode(ciphered_text):
    return ''.join([code_single(c) for c in ciphered_text])
