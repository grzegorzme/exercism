import string

def is_pangram(sentence):
    return all([a in sentence.lower() for a in string.ascii_lowercase])
