def main():
    groceries = {}
    while True:
        try:
            item = input().strip().upper()
        except EOFError:
            break
        if item:
            groceries[item] = groceries.get(item, 0) + 1

    for item in sorted(groceries):
        print(f"{groceries[item]} {item}")


if __name__ == "__main__":
    main()