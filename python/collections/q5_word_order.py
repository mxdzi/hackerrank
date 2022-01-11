from collections import defaultdict


def main():
    words = defaultdict(int)
    for _ in range(int(input())):
        words[input()] += 1

    print(len(words.keys()))
    print(' '.join(map(str, words.values())))


if __name__ == '__main__':
    main()
