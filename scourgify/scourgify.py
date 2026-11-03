import csv
import sys


def main():
    if valid_input():
        convert()


def convert():
    try:
        with open(sys.argv[1], encoding="utf-8") as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w", encoding="utf-8", newline="") as output:
                writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(",")
                    writer.writerow(
                        {
                            "first": first.strip(),
                            "last": last.strip(),
                            "house": row["house"],
                        }
                    )
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])


def valid_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    return True


if __name__ == "__main__":
    main()