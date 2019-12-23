import itertools


def main():
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    print(*itertools.product(a, b))


if __name__ == '__main__':
    main()
