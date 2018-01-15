import string
import itertools
import random


class Cipher(object):
    def __init__(self, key=None):
        if key is not None and all(c.islower() for c in key):
            self.key = key
        elif key is None:
            self.key = ''.join([random.choice(string.ascii_lowercase) for _ in range(100)])
        else:
            raise ValueError('Incorrect key provided')

    def shift(self, text, direction):
        key_gen = itertools.cycle(string.ascii_lowercase.index(k) for k in self.key)
        return ''.join([string.ascii_lowercase[
                            (string.ascii_lowercase.index(c.lower()) + direction * next(key_gen)) % len(string.ascii_lowercase)
                        ]
                        for c in text
                        if c.lower() in string.ascii_lowercase])

    def encode(self, text):
        return self.shift(text=text, direction=1)

    def decode(self, text):
        return self.shift(text=text, direction=-1)


class Caesar(Cipher):
    def __init__(self):
        super().__init__('d')
