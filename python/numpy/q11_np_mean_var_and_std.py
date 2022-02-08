import numpy


def main():
    n, m = list(map(int, input().split()))

    array = numpy.array([input().split() for _ in range(n)], int)

    numpy.set_printoptions(sign='-')
    print(numpy.mean(array, axis=1))
    print(numpy.var(array, axis=0))
    print(numpy.around(numpy.std(array), 11))


if __name__ == "__main__":
    main()
