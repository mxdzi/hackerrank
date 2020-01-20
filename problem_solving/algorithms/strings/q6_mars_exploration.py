#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the marsExploration function below.
def marsExploration(s):
    m = 'SOS'
    count = 0

    for i, c in enumerate(s):
        if c != m[i % 3]:
            count += 1
    return count


def main():
    s = input()

    result = marsExploration(s)

    print(str(result), sep='\n')


if __name__ == '__main__':
    main()
