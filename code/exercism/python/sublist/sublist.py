SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check_lists(first_list, second_list):
    is_sublist = '|'.join(str(e) for e in first_list) in '|'.join(str(e) for e in second_list)
    is_superlist = '|'.join(str(e) for e in second_list) in '|'.join(str(e) for e in first_list)

    return SUBLIST if is_sublist and not is_superlist else \
        SUPERLIST if not is_sublist and is_superlist else \
        EQUAL if is_sublist and is_superlist else UNEQUAL
