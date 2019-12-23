import itertools


def main():
    k, m = [int(i) for i in input().split()]

    print(max([sum([x ** 2 for x in p]) % m for p in
               itertools.product(*[[int(i) for i in input().split()[1:]] for _ in range(k)])]))


if __name__ == '__main__':
    main()
