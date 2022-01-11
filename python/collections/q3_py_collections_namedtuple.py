from collections import namedtuple


def main():
    n = int(input())
    Row = namedtuple('Row', input().split())
    s = 0
    for _ in range(n):
        s += int(Row(*input().split()).MARKS)
    print(f"{s / n:.02f}")


if __name__ == '__main__':
    main()
