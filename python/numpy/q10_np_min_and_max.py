import numpy


def main():
    n, m = list(map(int, input().split()))

    array = numpy.array([input().split() for _ in range(n)], int)

    print(numpy.max(numpy.min(array, axis=1)))


if __name__ == "__main__":
    main()
