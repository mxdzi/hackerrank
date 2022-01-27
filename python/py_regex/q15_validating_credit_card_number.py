import re


def main():
    valid = r"[456]\d{3}(-?\d{4}){3}$"
    no_repeats = r"((\d)-?(?!(-?\2){3})){16}"

    for _ in range(int(input())):
        card_number = input()
        if all(re.match(f, card_number) for f in [valid, no_repeats]):
            print("Valid")
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
