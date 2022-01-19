import re


def main():
    match = re.findall(r"(?<=[qwrtypsdfghjklzxcvbnm])[aieou]{2,}(?=[qwrtypsdfghjklzxcvbnm])", input(), flags=re.IGNORECASE)
    if match:
        for match in match:
            print(match)
    else:
        print("-1")


if __name__ == "__main__":
    main()
