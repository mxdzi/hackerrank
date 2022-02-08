import numpy


def main():
    N = int(input())
    array1 = numpy.array([input().split() for _ in range(N)], int)
    array2 = numpy.array([input().split() for _ in range(N)], int)

    print(numpy.dot(array1, array2))


if __name__ == "__main__":
    main()
