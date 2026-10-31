def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    input_user = input()
    result = convert(input_user)
    print(result)

main()