regex_pattern = r",|\."  # Do not delete 'r'.


import re


def main():
    print("\n".join(re.split(regex_pattern, input())))


if __name__ == '__main__':
    main()
