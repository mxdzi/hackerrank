#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
import operator
import functools


def lonelyinteger(a):
    return functools.reduce(operator.xor, a)


def main():
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(str(result), sep='\n')


if __name__ == '__main__':
    main()
