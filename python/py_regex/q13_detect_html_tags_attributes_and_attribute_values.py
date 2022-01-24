from html.parser import HTMLParser


class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->', ele[0], '>', ele[1])

    def error(self, message):
        pass


def main():
    parser = Parser()
    for _ in range(int(input())):
        parser.feed(input())


if __name__ == "__main__":
    main()
