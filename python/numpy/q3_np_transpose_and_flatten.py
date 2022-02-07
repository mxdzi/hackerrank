import numpy


def main():
    arr = []
    for _ in range(int(input().split()[0])):
        arr.append(input().split())

    arr = numpy.array(arr, int)

    print(arr.transpose())
    print(arr.flatten())


if __name__ == "__main__":
    main()
