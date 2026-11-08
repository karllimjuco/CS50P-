import sys
from datetime import date

import inflect


def main():
    birth = get_birth_date(input("Date of Birth: "))
    print(minutes_in_words(birth, date.today()))


def get_birth_date(text):
    try:
        year, month, day = text.split("-")
        return date(int(year), int(month), int(day))
    except (ValueError, TypeError):
        sys.exit("Invalid date")


def minutes_lived(birth, today):
    return (today - birth).days * 24 * 60


def minutes_in_words(birth, today):
    total = minutes_lived(birth, today)
    p = inflect.engine()
    words = p.number_to_words(total, andword="").capitalize()
    return f"{words} minutes"


if __name__ == "__main__":
    main()