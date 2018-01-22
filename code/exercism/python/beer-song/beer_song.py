def verse(number):
    base = ''
    if number > 1:
        base = '{orig_number} bottles of beer on the wall, {orig_number} bottles of beer.\n' \
               'Take one down and pass it around, {new_number} bottle{multiple} of beer on the wall.\n'
        base = base.format(
            orig_number=number,
            new_number='no more' if number == 1 else number-1,
            multiple='' if number == 2 else 's'
        )
    elif number == 1:
        base = '1 bottle of beer on the wall, 1 bottle of beer.\n' \
               'Take it down and pass it around, no more bottles of beer on the wall.\n'
    elif number == 0:
        base = 'No more bottles of beer on the wall, no more bottles of beer.\n' \
               'Go to the store and buy some more, 99 bottles of beer on the wall.\n'
    return base


def song(number1, number2=0):
    return '\n'.join(verse(i) for i in range(number1, number2-1, -1)) + '\n'
