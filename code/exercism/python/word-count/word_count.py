from collections import Counter
import string


def word_count(phrase):
    word_breaks = ' ,\n\t_'
    valid_chars = string.ascii_lowercase + word_breaks + "'0123456789"
    clean_phrase = ''.join(' ' if c in word_breaks else c for c in phrase.lower() if c in valid_chars)
    strip_quotes = [word.strip("'") for word in clean_phrase.split()]
    return dict(Counter(strip_quotes))
