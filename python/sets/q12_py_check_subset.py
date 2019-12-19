def main():
    for _ in range(int(input())):
        _ = input()
        a = set([int(i) for i in input().split()])
        _ = input()
        b = set([int(i) for i in input().split()])

        print(a.issubset(b))


if __name__ == "__main__":
    main()
