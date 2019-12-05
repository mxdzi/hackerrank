def main():
    N = int(input())

    commands = []

    for _ in range(N):
        commands.append(input())

    numbers = []

    for c in commands:
        c = c.split()
        if c[0] == 'insert':
            numbers.insert(int(c[1]), int(c[2]))
        if c[0] == 'remove':
            numbers.remove(int(c[1]))
        if c[0] == 'append':
            numbers.append(int(c[1]))
        if c[0] == 'sort':
            numbers.sort()
        if c[0] == 'reverse':
            numbers.reverse()
        if c[0] == 'pop':
            numbers.pop()
        if c[0] == 'print':
            print(numbers)
