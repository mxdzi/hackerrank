import re


def main():
    string = '\n'.join([input() for _ in range(int(input()))])
    string = re.sub(r"(?<= )\|\|(?= )", lambda x: "or", string)
    string = re.sub(r"(?<= )&&(?= )", lambda x: "and", string)
    print(string)


if __name__ == "__main__":
    main()
