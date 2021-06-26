alphabet_length = ord("z") - ord("a") + 1

def encode_char(x, a, b):
    x = ord(x.lower())
    if ord("a") <= x <= ord("z"):
        x = ord("a") + (a * (x - ord("a")) + b) % alphabet_length
        return chr(x)
    return ""

def encode(plain_text, a, b):
    return "".join(encode_char(x, a, b) for x in plain_text)


def decode(ciphered_text, a, b):
    return "".join((a ** -1) * (y - b) % alphabet_length for y in ciphered_text.lower())
