import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(
        r'<iframe[^>]*\ssrc="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"',
        s,
    )
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()