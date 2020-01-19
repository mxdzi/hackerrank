#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
from collections import deque


def hackerrankInString(s):
    d = deque("hackerrank")
    for c in s:
        if c == d[0]:
            d.popleft()
        if len(d) == 0:
            return 'YES'
    return 'NO'


def main():
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result, sep='\n')


if __name__ == '__main__':
    main()
