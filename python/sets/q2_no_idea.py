def main():
    n, m = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    set_a = set([int(i) for i in input().split()])
    set_b = set([int(i) for i in input().split()])

    happiness = 0

    for i in arr:
        if i in set_a:
            happiness += 1
        if i in set_b:
            happiness -= 1

    print(happiness)


if __name__ == "__main__":
    main()
