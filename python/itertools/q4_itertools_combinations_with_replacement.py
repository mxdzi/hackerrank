import itertools


def main():
    s, k = input().split()

    print(*[''.join(i) for i in itertools.combinations_with_replacement(sorted(s), int(k))], sep='\n')


if __name__ == '__main__':
    main()
