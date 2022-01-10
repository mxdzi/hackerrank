import collections


def main():
    _ = int(input())
    s = map(int, input().split())
    c = collections.Counter(s)
    amount = 0
    for _ in range(int(input())):
        size, price = map(int, input().split())
        if c.get(size, 0) > 0:
            amount += price
            c[size] = c[size] - 1
    print(amount)


if __name__ == '__main__':
    main()
