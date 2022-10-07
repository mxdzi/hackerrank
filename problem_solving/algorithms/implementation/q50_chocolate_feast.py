def chocolateFeast(n, c, m):
    total = n // c
    wraps = total
    while wraps >= m:
        total += wraps // m
        wraps = wraps // m + wraps % m
    return total
