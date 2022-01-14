import re


def fun(s):
    # return True if s is a valid email, else return False
    return re.match(r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", s)


def filter_mail(emails):
    return list(filter(fun, emails))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)

if __name__ == '__main__':
    main()

