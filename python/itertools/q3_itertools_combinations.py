import itertools


def main():
    s, k = input().split()

    print(*[''.join(j) for i in range(1, int(k) + 1) for j in itertools.combinations(sorted(s), i)], sep='\n')


if __name__ == '__main__':
    main()
