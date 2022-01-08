#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    from collections import Counter
    # Write your code here
    if len(s) % 2 == 1:
        return -1

    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]

    c1 = Counter(s1)
    c2 = Counter(s2)

    return sum((c2 - c1).values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
