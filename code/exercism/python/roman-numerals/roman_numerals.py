def numeral(number):
    result = 'I' * number
    result = result.replace('IIIII', 'V')
    result = result.replace('IIII', 'IV')
    result = result.replace('VV', 'X')
    result = result.replace('VIV', 'IX')
    result = result.replace('XXXXX', 'L')
    result = result.replace('XXXX', 'XL')
    result = result.replace('LL', 'C')
    result = result.replace('LXL', 'XC')
    result = result.replace('CCCCC', 'D')
    result = result.replace('CCCC', 'CD')
    result = result.replace('DD', 'M')
    result = result.replace('DCD', 'CM')
    return result
