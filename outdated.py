MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def main():
    while True:
        date = input("Date: ").strip()
        result = convert(date)
        if result:
            print(result)
            break


def convert(date):
    if "/" in date:
        parts = date.split("/")
        if len(parts) != 3:
            return None
        month, day, year = parts
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            return None
        month, day = int(month), int(day)
    elif "," in date:
        try:
            month_name, rest = date.split(" ", 1)
            day, year = rest.split(",")
        except ValueError:
            return None
        month_name = month_name.strip()
        day = day.strip()
        year = year.strip()
        if month_name not in MONTHS or not day.isdigit() or not year.isdigit():
            return None
        month = MONTHS.index(month_name) + 1
        day = int(day)
    else:
        return None

    if not (1 <= month <= 12 and 1 <= day <= 31):
        return None

    return f"{int(year):04}-{month:02}-{day:02}"


if __name__ == "__main__":
    main()