def main():
    Regex_Pattern = r'^[^1234567890][^aeiou][^bcDF][^\s][^AEIOU][^\.,]$'

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
