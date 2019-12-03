def diagonalDifference(arr):
    dd = 0
    du = 0
    length = len(arr)
    for i, line in enumerate(arr):
        dd = dd + line[i]
        du = du + line[length - 1 - i]

    return abs(dd - du)
