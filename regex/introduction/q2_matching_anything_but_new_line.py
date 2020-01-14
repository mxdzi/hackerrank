def main():
    regex_pattern = r"...\....\....\....$"

    import re
    import sys

    test_string = input()

    match = re.match(regex_pattern, test_string) is not None

    print(str(match).lower())


if __name__ == '__main__':
    main()
