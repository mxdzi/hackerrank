def main():
    Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
