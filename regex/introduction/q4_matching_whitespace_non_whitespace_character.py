def main():
    Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
