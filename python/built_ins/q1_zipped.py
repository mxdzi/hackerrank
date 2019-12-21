def main():
    n, x = [int(i) for i in input().split()]

    scores = []
    for s in range(x):
        scores.append([float(i) for i in input().split()])

    for s in zip(*scores):
        print(sum(s) / len(s))


if __name__ == '__main__':
    main()
