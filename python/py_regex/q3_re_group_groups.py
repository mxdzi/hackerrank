import re


def main():
    match = re.search(r"([a-zA-Z0-9])\1", input())
    if match:
        print(match.group(1))
    else:
        print("-1")


if __name__ == "__main__":
    main()
