from string import ascii_lowercase


def print_rangoli(size):
    letters = [ascii_lowercase[i] for i in range(size)]
    letters = list(reversed(letters))[:-1] + letters
    middle = len(letters) // 2
    width = (size - 1) * 4 + 1

    for i in reversed(range(size - 1)):
        print(
            ('-'.join(letters[:middle - i] + letters[middle + i + 2:])).center(width, '-'))

    print('-'.join(letters))

    for i in range(size - 1):
        print(
            ('-'.join(letters[:middle - i] + letters[middle + i + 2:])).center(width, '-'))
