from string import ascii_uppercase


def camelcase(s):
    count = 1
    for char in s:
        if char in ascii_uppercase:
            count += 1
    return count
