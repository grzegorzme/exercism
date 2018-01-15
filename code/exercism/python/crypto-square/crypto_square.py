import string
import numpy as np


def encode(plain_text):
    normalized_text = [a for a in plain_text.lower()
                       if a in string.ascii_lowercase + '0123456789']
    if len(normalized_text) == 0:
        return ''
    c = int(np.ceil(np.sqrt(len(normalized_text))))
    r = int(np.ceil(len(normalized_text) / c))

    normalized_text += [' ' for _ in range(r*c - len(normalized_text))]

    return ' '.join([''.join(row) for row in np.reshape(normalized_text, (r, c)).T])
