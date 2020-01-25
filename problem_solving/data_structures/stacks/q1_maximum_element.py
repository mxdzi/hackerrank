def main():
    s = []
    for _ in range(int(input())):
        q = input().split()
        if q[0] == '1':
            if len(s):
                s.append(max(s[-1], int(q[1])))
            else:
                s.append(int(q[1]))
        elif q[0] == '2' and len(s):
            s.pop()
        elif q[0] == '3' and len(s):
            print(s[-1])


if __name__ == "__main__":
    main()
