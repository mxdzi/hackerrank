import re


def main():
    for s in range(int(input())):
        r = input()

        try:
            re.compile(r)
            print("True")
        except re.error:
            print("False")


if __name__ == '__main__':
    main()
