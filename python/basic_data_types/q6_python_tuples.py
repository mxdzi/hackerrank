def main():
    n = int(input())
    integer_list = map(int, input().split())

    print(hash((*integer_list,)))
