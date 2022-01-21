import email.utils
import re


def main():
    for _ in range(int(input())):
        name, address = email.utils.parseaddr(input())
        if re.match(r"[a-z][a-z-._0-9]*@[a-z]+\.[a-z]{1,3}$", address):
            print(email.utils.formataddr((name, address)))


if __name__ == "__main__":
    main()
