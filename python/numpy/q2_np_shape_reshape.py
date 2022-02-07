import numpy


def arrays(arr):
    return numpy.reshape(numpy.array(arr, int), (3, 3))


def main():
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)


if __name__ == "__main__":
    main()
