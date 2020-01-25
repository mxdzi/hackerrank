#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
from collections import deque


def isBalanced(s):
    d = deque()
    pairs = {'(': ')', '[': ']', '{': '}'}

    if not s:
        return 'NO'
    for c in s:
        if c in pairs.keys():
            d.append(c)
        else:
            if not d or pairs[d.pop()] != c:
                return 'NO'
    if d:
        return 'NO'
    return 'YES'


def main():
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result, sep='\n')


if __name__ == '__main__':
    main()
