#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    def is_power2(n):
        return bool(n and not (n & (n - 1)))

    step = 0
    if n == 1:
        return "Richard"

    while n > 1:
        if is_power2(n):
            n = n // 2
        else:
            n = n - int('1' + '0' * len(bin(n)[3:]), base=2)
        if n == 1:
            if step % 2:
                return "Richard"
            else:
                return "Louise"
        step += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
