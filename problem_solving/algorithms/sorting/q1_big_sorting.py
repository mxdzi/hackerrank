#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bigSorting function below.
def bigSorting(unsorted):
    return sorted(sorted(unsorted), key=len)


def main():
    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print('\n'.join(result))


if __name__ == '__main__':
    main()
