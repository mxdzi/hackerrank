#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the winningLotteryTicket function below.

def winningLotteryTicket(tickets):
    d = dict()
    for t in tickets:
        s = frozenset(t)
        d[s] = d.get(s, 0) + 1
    l = list(d.keys())

    counter = 0
    for i in range(0, len(l)):
        for j in range(i + 1, len(l)):

            if len(l[i] | l[j]) == 10:
                counter += d[l[i]] * d[l[j]]
        if len(l[i]) == 10:
            counter += (d[l[i]] * (d[l[i]] - 1)) // 2
    return counter


def main():
    n = int(input())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    print(str(result) + '\n')


if __name__ == '__main__':
    main()
