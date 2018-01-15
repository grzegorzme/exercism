suffixes = ['thousand', 'million', 'billion']

simple = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']


def say_to_20(number):
    return simple[number]


def say_to_100(number):
    if number < 20:
        return say_to_20(number)
    else:
        if number % 10 == 0:
            return tens[number % 100 // 10]
        else:
            return tens[number % 100 // 10] + '-' + say_to_20(number % 10)


def say_to_1000(number):
    if number < 100:
        return say_to_100(number)
    else:
        if number % 100 == 0:
            return say_to_20(number // 100) + ' hundred'
        else:
            return say_to_20(number // 100) + ' hundred and ' + say_to_100(number % 100)


def say(number):
    number = int(number)

    if not 0 <= number < 10**12:
        raise ValueError('Invalid input!')

    if number == 0:
        return 'zero'

    i = number
    blocks = []
    while i > 0:
        blocks.append(i % 1000)
        i //= 1000
    blocks = list(reversed(blocks))

    number_name = str(say_to_1000(blocks[-1]))
    if number > 999 and 0 < blocks[-1] < 100:
        number_name = 'and ' + number_name

    for suffix, block in zip(suffixes, blocks[::-1][1:]):
        if block != 0:
            if number_name == '':
                number_name = say_to_1000(block) + ' ' + suffix
            else:
                number_name = say_to_1000(block) + ' ' + suffix + ' ' + number_name

    return number_name
