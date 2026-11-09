import csv
import random
import sys


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "cards.csv"

    try:
        cards = load_cards(filename)
    except FileNotFoundError:
        sys.exit(f"Could not find {filename}")

    if not cards:
        sys.exit("No flashcards found in the file.")

    random.shuffle(cards)
    correct, missed = quiz(cards)
    total = len(cards)
    print(f"\nScore: {correct}/{total} ({calculate_score(correct, total):.0f}%)")

    if missed and input("Retry the cards you missed? (y/n) ").strip().lower() == "y":
        weak_cards = pick_weak_cards(cards, missed)
        correct, missed = quiz(weak_cards)
        total = len(weak_cards)
        print(f"\nRetry score: {correct}/{total} ({calculate_score(correct, total):.0f}%)")


def quiz(cards):
    """Ask each card in turn. Return (number correct, list of missed questions)."""
    correct = 0
    missed = []

    for question, answer in cards:
        if check_answer(input(f"{question} "), answer):
            print("Correct!")
            correct += 1
        else:
            print(f"Wrong. The answer is: {answer}")
            missed.append(question)

    return correct, missed


def load_cards(filename):
    """Read a CSV file of question,answer rows and return a list of (question, answer) tuples."""
    cards = []

    with open(filename, newline="", encoding="utf-8") as file:
        for row in csv.reader(file):
            if len(row) >= 2 and row[0].strip():
                cards.append((row[0].strip(), row[1].strip()))

    return cards


def check_answer(user_answer, correct_answer):
    """Compare answers, ignoring case and extra spaces."""
    return user_answer.strip().lower() == correct_answer.strip().lower()


def calculate_score(correct, total):
    """Return the score as a percentage."""
    if total == 0:
        return 0.0
    return correct / total * 100


def pick_weak_cards(cards, missed):
    """Return only the cards whose question is in the missed list."""
    return [card for card in cards if card[0] in missed]


if __name__ == "__main__":
    main()