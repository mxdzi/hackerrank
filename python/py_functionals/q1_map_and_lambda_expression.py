cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def main():
    n = int(input())
    print(list(map(cube, fibonacci(n))))


if __name__ == '__main__':
    main()
