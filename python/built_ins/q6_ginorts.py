from string import ascii_lowercase, ascii_uppercase, digits


def main():
    s = input()

    lowercase = ''.join(sorted([i for i in s if i in ascii_lowercase]))
    uppercase = ''.join(sorted([i for i in s if i in ascii_uppercase]))
    odd = ''.join(sorted([i for i in s if i in digits and int(i) % 2 == 1]))
    even = ''.join(sorted([i for i in s if i in digits and int(i) % 2 == 0]))

    print(lowercase + uppercase + odd + even)


if __name__ == "__main__":
    main()
