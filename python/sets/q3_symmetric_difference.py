def main():
    _ = int(input())
    n = set(map(int, input().split()))
    _ = int(input())
    m = set(map(int, input().split()))

    print(*sorted(n.symmetric_difference(m)), sep='\n')


if __name__ == '__main__':
    main()
