def main():
    n = int(input())
    countries = [input() for _ in range(n)]
    print(len(set(countries)))


if __name__ == "__main__":
    main()
