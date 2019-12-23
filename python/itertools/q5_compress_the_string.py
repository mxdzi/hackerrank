import itertools


def main():
    s = input()

    print(*[(len(list(g[1])), int(g[0])) for g in itertools.groupby(s)])


if __name__ == '__main__':
    main()
