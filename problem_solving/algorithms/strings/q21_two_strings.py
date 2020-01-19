#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return 'YES' if len(s1.intersection(s2)) > 0 else 'NO'


def main():
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result, sep='\n')


if __name__ == '__main__':
    main()
