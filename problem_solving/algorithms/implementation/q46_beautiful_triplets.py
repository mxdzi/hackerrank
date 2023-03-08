from collections import Counter


def beautifulTriplets(d, arr):
    count = Counter(arr)
    total = 0
    for num in filter(lambda x: (x+d in arr) and (x-d in arr), arr):
        total += max(count[num+3], count[num], count[num-3])
    return total
