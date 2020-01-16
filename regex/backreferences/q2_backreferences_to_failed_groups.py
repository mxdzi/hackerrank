def main():
    Regex_Pattern = r"^\d{2}(-?)\d{2}(\1)\d{2}(\1)\d{2}$"

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
