#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flippingBits function below.
def flippingBits(n):
    return int("{:032b}".format(n).translate(str.maketrans('01', '10')), 2)


def main():
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        print(str(result), sep='\n')


if __name__ == '__main__':
    main()
