def main():
    time = convert(input("What time is it? ").strip())
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    clean_time = time.replace("a.m.", "").replace("p.m.", "").strip()
    if ":" in clean_time:
        hours, minutes = map(int, clean_time.split(":"))
    else:
        hours, minutes = int(clean_time), 0
    if "p.m." in time and hours != 12:
        hours += 12
    if "a.m." in time and hours == 12:
        hours = 0
    return hours + minutes / 60


if __name__ == "__main__":
    main()