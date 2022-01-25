import re


def main():
    no_repeats = r"(?!.*(.).*\1)"
    two_or_more_upper = r"(.*[A-Z]){2,}"
    three_or_more_digits = r"(.*\d){3,}"
    ten_alphanumerics = r"[a-zA-Z0-9]{10}"

    for _ in range(int(input())):
        uuid = input()
        if all(re.match(f, uuid) for f in [no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics]):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
