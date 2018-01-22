presents = {
    1: ('first', 'a Partridge in a Pear Tree'),
    2: ('second', 'two Turtle Doves'),
    3: ('third', 'three French Hens'),
    4: ('fourth', 'four Calling Birds'),
    5: ('fifth', 'five Gold Rings'),
    6: ('sixth', 'six Geese-a-Laying'),
    7: ('seventh', 'seven Swans-a-Swimming'),
    8: ('eighth', 'eight Maids-a-Milking'),
    9: ('ninth', 'nine Ladies Dancing'),
    10: ('tenth', 'ten Lords-a-Leaping'),
    11: ('eleventh', 'eleven Pipers Piping'),
    12: ('twelfth', 'twelve Drummers Drumming'),
}


def verse(day_number):
    return 'On the {day} day of Christmas my true love gave to me, {presents}.\n'.format(
        day=presents[day_number][0],
        presents=', '.join(
            [('and ' if i == 1 and day_number > 1 else '') + presents[i][1] for i in range(day_number, 0, -1)]
        )
    )


def verses(start, end):
    return '\n'.join(verse(i) for i in range(start, end + 1)) + '\n'


def sing():
    return verses(1, 12)
