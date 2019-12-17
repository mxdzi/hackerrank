def main():
    n = int(input())
    s = set(map(int, input().split()))

    i = int(input())
    for i in range(i):
        command = input().split()
        if command[0] == 'pop':
            s.pop()
        if command[0] == 'remove':
            try:
                s.remove(int(command[1]))
            except KeyError:
                pass
        if command[0] == 'discard':
            s.discard(int(command[1]))

    print(sum(s))


if __name__ == "__main__":
    main()
