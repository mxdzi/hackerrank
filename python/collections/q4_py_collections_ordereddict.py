from collections import OrderedDict


def main():
    items = OrderedDict()
    for _ in range(int(input())):
        name, price = input().rsplit(' ', 1)
        items[name] = items.get(name, 0) + int(price)
    for name, price in items.items():
        print(name, price)


if __name__ == '__main__':
    main()
