from collections import defaultdict


def main():
    a, b = map(int, input().split())
    d = defaultdict(list)
    for i in range(a):
        w = input()
        d[w].append(i + 1)
    for _ in range(b):
        w = input()
        print(' '.join(map(str, d.get(w, [-1]))))


if __name__ == '__main__':
    main()
