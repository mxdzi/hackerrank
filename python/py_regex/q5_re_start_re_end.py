import re


def main():
    S = input()
    k = input()
    pattern = re.compile(k)
    r = pattern.search(S)
    if not r:
        print((-1, -1))
    while r:
        print((r.start(), r.end() - 1))
        r = pattern.search(S, r.start() + 1)


if __name__ == "__main__":
    main()
