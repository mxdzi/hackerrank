#!/bin/python3

import sys


def examRush(tm, t):
    chapters = sorted(tm)
    time = 0
    count = 0
    while time + chapters[0] <= t:
        time += chapters.pop(0)
        count += 1
    return count


def main():
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    tm = []
    tm_i = 0
    for tm_i in range(n):
        tm_t = int(input().strip())
        tm.append(tm_t)
    result = examRush(tm, t)
    print(result)


if __name__ == "__main__":
    main()
