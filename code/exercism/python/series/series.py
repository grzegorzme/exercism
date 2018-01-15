def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError('Invalid subseries length')
    else:
        return [[int(o) for o in (series[k:(k+length)])] for k in range(len(series)-length+1)]
