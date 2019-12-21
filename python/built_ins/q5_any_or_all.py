def main():
    _ = input()
    arr = input().split()

    print(all([int(i) > 0 for i in arr]) and any([i == i[::-1] for i in arr]))


if __name__ == "__main__":
    main()
