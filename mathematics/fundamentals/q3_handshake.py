#!/bin/python3

import os
import sys

#
# Complete the handshake function below.
#


def handshake(n):
    return ((n - 1) * n) // 2


def main():
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        print(str(result), sep='\n')


if __name__ == '__main__':
    main()
