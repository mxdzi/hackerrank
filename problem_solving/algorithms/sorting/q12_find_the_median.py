#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findMedian function below.
def findMedian(arr):
    return sorted(arr)[len(arr)//2]


def main():
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(str(result), sep='\n')


if __name__ == '__main__':
    main()
