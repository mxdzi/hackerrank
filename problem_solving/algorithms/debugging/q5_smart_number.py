import math


def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False


def main():
    for _ in range(int(input())):
        num = int(input())
        ans = is_smart_number(num)
        if ans:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
