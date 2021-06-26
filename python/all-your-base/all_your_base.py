def rebase(input_base, digits, output_base):
    if not all(0 <= d < input_base for d in digits):
        raise ValueError("Invalid digits for this input_base")
    if input_base < 2 or output_base < 2:
        raise ValueError("Invalid bases - should be positive numbers")

    number = sum(x * (input_base ** k) for k, x in enumerate(digits[::-1]))

    result = list()
    while number >= output_base:
        r = number % output_base
        result.append(r)
        number = (number - r) // output_base
    result.append(number)

    return result[::-1]
