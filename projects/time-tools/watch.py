import re
import sys


def main():
    s = input("HTML: ").strip()
    print(parse(s))

def parse(s):
    match = re.search(r'<iframe[^>]*src="(http:|https:)//(www\.)?youtube\.com/embed/(\w+)"', s)
    if not match:
        return None
    else:
        return (f"https://youtu.be/{match.group(3)}")





if __name__ == "__main__":
    main()

