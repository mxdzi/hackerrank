import numpy


def main():
    poly = numpy.array(input().split(), float)
    val = int(input())

    print(numpy.polyval(poly, val))


if __name__ == "__main__":
    main()
