import numpy


def main():
    N = int(input())
    array = numpy.array([input().split() for _ in range(N)], float)
    numpy.set_printoptions(legacy='1.13')
    print(numpy.linalg.det(array))


if __name__ == "__main__":
    main()
