def viralAdvertising(n):
    total = 0
    shared = 5
    day = 1
    while day <= n:
        liked = shared // 2
        total += liked
        shared = (shared // 2) * 3
        day += 1
    return total
