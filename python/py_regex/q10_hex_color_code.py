import re


def main():
    for _ in range(int(input())):
        for match in re.findall(r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", input(), re.IGNORECASE):
            print(match)


if __name__ == "__main__":
    main()
