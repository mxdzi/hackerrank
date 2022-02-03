#!/bin/python3

import math
import os
import random
import re
import sys



def main():
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    s = ""

    for i in range(m):
        for j in matrix:
            s += j[i]

    print(re.sub(r'(?<=\w)(\W+)(?=\w)', ' ', s))

if __name__ == "__main__":
    main()
