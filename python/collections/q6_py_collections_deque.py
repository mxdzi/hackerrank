from collections import deque


def main():
    d = deque()
    for _ in range(int(input())):
        command, __, value = input().partition(' ')
        if command == 'append':
            d.append(value)
        elif command == 'appendleft':
            d.appendleft(value)
        elif command == 'pop':
            d.pop()
        elif command == 'popleft':
            d.popleft()
    print(' '.join(d))


if __name__ == "__main__":
    main()
