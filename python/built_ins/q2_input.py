def main():
    x, k = [int(i) for i in input().split()]
    p = input()

    print(eval(p) == k)


if __name__ == '__main__':
    main()
