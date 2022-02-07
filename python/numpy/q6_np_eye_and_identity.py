import numpy


def main():
    nums = tuple(map(int, input().split()))
    print(numpy.eye(*nums, k=0))


if __name__ == "__main__":
    main()
