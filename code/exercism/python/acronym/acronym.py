import string


def abbreviate(words):
    parts = words.split(':')
    if parts[0].isupper():
        return parts[0]
    else:
        return ''.join(l for l in words.title() if l in string.ascii_uppercase)
