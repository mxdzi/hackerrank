def main():
    Regex_Pattern = r'[a-zA-Z02468]{40}[13579\s]{5}$'

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
