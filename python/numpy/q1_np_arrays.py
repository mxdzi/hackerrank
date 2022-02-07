import numpy


def arrays(arr):
    return numpy.flipud(numpy.array(arr, float))


def main():
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)


if __name__ == "__main__":
    main()
