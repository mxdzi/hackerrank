import re


def main():
    for _ in range(int(input())):
        print("YES" if re.match(r"^[789]\d{9}$", input()) else "NO")


if __name__ == "__main__":
    main()
