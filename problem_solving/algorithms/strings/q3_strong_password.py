def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    password_set = set(password)
    count = 0

    if not any(c in numbers for c in password_set):
        count += 1
    if not any(c in lower_case for c in password_set):
        count += 1
    if not any(c in upper_case for c in password_set):
        count += 1
    if not any(c in special_characters for c in password_set):
        count += 1
    if len(password) + count < 6:
        count += 6 - len(password) - count
    return count
