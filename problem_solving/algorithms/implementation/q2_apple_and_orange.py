def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0

    for apple in apples:
        if t >= apple + a >= s:
            count_apples += 1
    for orange in oranges:
        if t >= orange + b >= s:
            count_oranges += 1
    print(count_apples)
    print(count_oranges)
