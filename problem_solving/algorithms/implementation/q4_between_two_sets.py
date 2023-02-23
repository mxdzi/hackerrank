def getTotalX(a, b):
    array = [i for i in range(max(a), min(b) + 1)]
    array2 = [i for i in array if all(i % j == 0 for j in a)]
    array3 = [i for i in array2 if all(j % i == 0 for j in b)]

    return len(array3)
