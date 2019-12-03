import sys

def plusMinus(arr):
    p1 = [a for a in arr if a > 0]
    p2 = [b for b in arr if b < 0]
    p3 = [c for c in arr if c == 0]

    r = ['{:f}'.format(len(p1) / len(arr)), '{:f}'.format(len(p2) / len(arr)), '{:f}'.format(len(p3) / len(arr))]
    for i in r:
        sys.stdout.write(i + '\n')
