def countingValleys(steps, path):
    v = 0
    c = 0
    for s in path:
        if s == 'U':
            v += 1
        else:
            v -= 1
        if v == 0 and s == 'U':
            c += 1
    return c
