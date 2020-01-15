def main():
    Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
