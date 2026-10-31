
phrase = input("Greeting: ").lstrip().lower()

if phrase.startswith("hello"):
    print("$0")
elif phrase.startswith("h"):
    print("$20")
else:
    print("$100")