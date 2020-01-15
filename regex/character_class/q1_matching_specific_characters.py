def main():
    Regex_Pattern = r'^[123][012][sx0][03aA][sxu][\.,]$'

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
