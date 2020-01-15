def main():
    Regex_Pattern = r'^\d{1,2}[a-zA-z]{3,}\.{0,3}$'

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
