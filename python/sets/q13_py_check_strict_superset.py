def main():
    a = set(input().split())

    for i in range(int(input())):
        s = set(input().split())

        if len(s.difference(a)) != 0 or len(a) <= len(s):
            print("False")
            break
    else:
        print("True")


if __name__ == "__main__":
    main()
