def main():
    for _ in range(int(input())):
        n, m = [int(s) for s in input().split()]

        matrix = dict()

        for _ in range(m):
            command = input()
            if command.startswith('UPDATE'):
                arg = command.split()
                matrix[(int(arg[1]), int(arg[2]), int(arg[3]))] = int(arg[4])
            if command.startswith('QUERY'):
                arg = command.split()
                print(sum([v for k, v in matrix.items()
                           if int(arg[1]) <= k[0] <= int(arg[4])
                           and int(arg[2]) <= k[1] <= int(arg[5])
                           and int(arg[3]) <= k[2] <= int(arg[6])]))


if __name__ == '__main__':
    main()
