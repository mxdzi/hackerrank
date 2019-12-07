def main():
    n, m = [int(i) for i in input().split()]

    for i in range(n // 2):
        print(('.|.' * (i * 2 + 1)).center(m, '-'))

    print("WELCOME".center(m, '-'))

    for i in reversed(range(n // 2)):
        print(('.|.' * (i * 2 + 1)).center(m, '-'))


if __name__ == "__name__":
    main()
