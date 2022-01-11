from collections import deque


def pile_up(l):
    d = deque(l)
    last = max(d[0], d[-1])
    while d:
        if d[0] >= d[-1]:
            if d[0] > last:
                return "No"
            d.popleft()
        elif d[0] < d[-1]:
            if d[-1] > last:
                return "No"
            d.pop()
    else:
        return "Yes"


def main():
    for _ in range(int(input())):
        __ = input()
        print(pile_up(map(int, input().split())))


if __name__ == "__main__":
    main()
