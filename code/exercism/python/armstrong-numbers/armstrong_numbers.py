def is_armstrong(number):
    return number == sum(int(c)**len(str(number)) for c in str(number))
