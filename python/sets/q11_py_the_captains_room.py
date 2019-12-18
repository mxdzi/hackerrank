def main():
    _ = input()
    k = input().split()
    d = {}
    for i in k:
        d[i] = d.get(i, 0) + 1

    print(min(d, key=d.get))


if __name__ == "__main__":
    main()
