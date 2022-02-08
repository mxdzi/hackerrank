import numpy


def main():
    N, M = list(map(int, input().split()))
    array = [numpy.array(input().split(), int) for _ in range(N)]

    print(numpy.product(numpy.sum(array, axis=0)))


if __name__ == "__main__":
    main()
