def main():
    items = {}

    while True:
        try:
            item = input().strip()
        except EOFError:
            break

        item = item.lower()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1


    for item in sorted(items):
        print(items[item], item.upper())


main()
