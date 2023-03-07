def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        dt = 0
        if (i + m) > len(s):
            break
        for j in range(i, i + m):
            dt += s[j]
        if dt == d:
            count += 1
    return count
