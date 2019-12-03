def divisibleSumPairs(n, k, ar):
    s = 0
    for i, _ in enumerate(ar):
        for j, _ in enumerate(ar):
            if i < j:
                if (ar[i] + ar[j]) % k == 0:
                    s += 1
    return s
