def main():
    t = int(input())

    for s in range(t):
        a, b = input().split()

        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)


if __name__ == '__main__':
    main()
