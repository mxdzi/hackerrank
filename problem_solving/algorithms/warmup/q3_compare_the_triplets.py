def compareTriplets(a, b):
    p1 = 0
    p2 = 0
    for points in zip(a, b):
        if points[0] == points[1]:
            continue
        if points[0] > points[1]:
            p1 += 1
        else:
            p2 += 1
    return [p1, p2]
