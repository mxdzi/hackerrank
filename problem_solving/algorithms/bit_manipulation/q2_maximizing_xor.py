#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
import itertools
import operator


def maximizingXor(l, r):
    return max(operator.xor(*i) for i in list(itertools.combinations_with_replacement(range(l, r + 1), 2)))


def main():
    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    print(str(result), sep='\n')


if __name__ == '__main__':
    main()
