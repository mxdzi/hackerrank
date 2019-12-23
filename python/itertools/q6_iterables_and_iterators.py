import itertools


def main():
    n = int(input())
    s = input().split()
    k = int(input())

    count = 0
    length = 0
    for i in itertools.combinations(s, k):
        if 'a' in i:
            count += 1
        length += 1

    print('{:.4f}'.format(count / length))


if __name__ == '__main__':
    main()
