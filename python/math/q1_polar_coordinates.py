import cmath


def main():
    c = complex(input())

    print(abs(c))
    print(cmath.phase(c))


if __name__ == "__main__":
    main()
