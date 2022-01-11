#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def main():
    c = Counter(sorted(list(input())))
    print(*(f"{k} {v}" for k, v in c.most_common(3)), sep='\n')


if __name__ == '__main__':
    main()
