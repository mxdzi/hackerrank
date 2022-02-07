import numpy


def main():
    array = numpy.array(input().split(), float)

    numpy.set_printoptions(sign=' ')
    print(numpy.floor(array))
    print(numpy.ceil(array))
    print(numpy.rint(array))


if __name__ == "__main__":
    main()
