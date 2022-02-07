import numpy


def main():
    nums = tuple(map(int, input().split()))
    print(numpy.zeros(nums, int))
    print(numpy.ones(nums, int))


if __name__ == "__main__":
    main()
