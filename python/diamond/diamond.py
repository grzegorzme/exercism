def rows(letter):
    end = ord(letter) - ord("A")
    row_length = 2 * end + 1
    center = row_length // 2
    result = list()

    for k in range(end + 1):
        row = [" "] * row_length
        row[center - k] = row[center + k] = chr(ord("A") + k)
        result.append("".join(row))

    return result + result[:-1][::-1]
