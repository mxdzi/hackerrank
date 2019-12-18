def main():
    _ = input()
    n = set(input().split())
    _ = input()
    b = set(input().split())

    print(len(n.symmetric_difference(b)))


if __name__ == "__main__":
    main()
