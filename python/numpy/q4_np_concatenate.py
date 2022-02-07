import numpy


def main():
    N, M, P = map(int, input().split())
    array1 = numpy.array([input().split() for _ in range(N)], int)
    array2 = numpy.array([input().split() for _ in range(M)], int)

    print(numpy.concatenate((array1, array2)))


if __name__ == "__main__":
    main()
