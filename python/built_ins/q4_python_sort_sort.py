import math
import os
import random
import re
import sys


def main():
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for a in sorted(arr, key=lambda x: x[k]):
        print(' '.join([str(s) for s in a]))


if __name__ == '__main__':
    main()
