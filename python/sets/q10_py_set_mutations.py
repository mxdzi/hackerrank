def main():
    _ = input()
    a = set([int(i) for i in input().split()])

    for _ in range(int(input())):
        command = input().split()[0]
        s = set([int(i) for i in input().split()])
        if command == 'update':
            a.update(s)
        elif command == 'intersection_update':
            a.intersection_update(s)
        elif command == 'difference_update':
            a.difference_update(s)
        elif command == 'symmetric_difference_update':
            a.symmetric_difference_update(s)

    print(sum(a))


if __name__ == "__main__":
    main()
