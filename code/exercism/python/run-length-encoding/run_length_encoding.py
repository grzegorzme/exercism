import re


def decode(string):
    """
        find a series of digits (group 1) followed by a single char (group 2)
        single chars (no preceding digits) are left unchanged
    """
    pattern = r'(\d+)(\D)'
    return re.sub(pattern, lambda m: int(m.group(1)) * m.group(2), string)


def encode(string):
    """
        find any character and check if its followed by more occurrences of itself
    """
    pattern = r'(\D)\1{1,}'
    return re.sub(pattern, lambda m: str(len(m.group())) + m.group()[0], string)
