import math


def main():
    ab = int(input())
    bc = int(input())

    print("{}°".format(round(math.degrees(math.atan(ab / bc)))))


if __name__ == "__main__":
    main()
