import calendar


def main():
    s = [int(i) for i in input().split()]
    print(calendar.day_name[calendar.weekday(s[2], s[0], s[1])].upper())


if __name__ == '__main__':
    main()
