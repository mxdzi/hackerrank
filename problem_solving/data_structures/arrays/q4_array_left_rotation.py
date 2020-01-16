#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque


def arr_left_rotate(a, d):
    l = deque(a)
    l.rotate(-d)
    print(' '.join([str(s) for s in l]))


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
