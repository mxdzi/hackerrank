import numpy


def main():
    N, M = list(map(int, input().split()))

    arrayA = numpy.array([input().split() for _ in range(N)], int)
    arrayB = numpy.array([input().split() for _ in range(N)], int)

    print(arrayA + arrayB)
    print(arrayA - arrayB)
    print(arrayA * arrayB)
    print(arrayA // arrayB)
    print(arrayA % arrayB)
    print(arrayA ** arrayB)


if __name__ == "__main__":
    main()
