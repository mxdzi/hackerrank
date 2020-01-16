def main():
    Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-z])([aeiouAEIOU])(\S)(\1)(\2)(\3)(\4)(\5)(\6)(\7)(\8)(\9)(\10)'

    import re

    print(str(bool(re.search(Regex_Pattern, input()))).lower())


if __name__ == '__main__':
    main()
