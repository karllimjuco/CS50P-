# Flash Me
#### Video Demo: https://youtu.be/LO4IFx9vsQw
#### Description:

Flash Me is a command-line flashcard quiz written in Python. It loads a deck of questions and answers from a CSV file, quizzes you in random order, tells you whether each answer is right, and shows your score at the end. If you missed any cards, it offers to quiz you again on only those cards, so you spend your time on your weak spots. I built it to help me study for my IT certifications, but it works for any subject because the deck is just a text file.

## How to run it

Install the one dependency, which is only needed for the tests, with `pip install -r requirements.txt`. Then run `python project.py` to use the default deck, `cards.csv`, or `python project.py mydeck.csv` to use your own. Each line of a deck is a question and its answer separated by a comma, for example `What does DNS stand for?,Domain Name System`. Questions should not contain commas. To run the tests, use `pytest test_project.py`.

## What each file does

**project.py** holds the whole program. `main()` reads the deck's filename from the command line (falling back to `cards.csv`), loads the cards, exits with a clear message if the file is missing or empty, shuffles the cards, runs the quiz, prints the score, and asks whether to retry the missed cards. Besides `main()`, it has five functions:

- `quiz(cards)` asks each card in turn, prints whether the answer was right, and returns the number correct plus a list of the questions that were missed.
- `load_cards(filename)` reads the CSV and returns a list of (question, answer) tuples. It strips extra spaces and skips blank lines and rows that don't have both a question and an answer.
- `check_answer(user_answer, correct_answer)` compares the two answers while ignoring capital letters and extra spaces.
- `calculate_score(correct, total)` returns the score as a percentage, and returns 0 when there are no cards so the program never divides by zero.
- `pick_weak_cards(cards, missed)` returns only the cards whose questions were missed, which becomes the deck for the retry round.

**test_project.py** contains pytest tests for the four functions that don't depend on user input: `load_cards`, `check_answer`, `calculate_score`, and `pick_weak_cards`. The `load_cards` test uses pytest's temporary-file fixture so it never touches a real deck, and it also checks that a missing file raises `FileNotFoundError`.

**cards.csv** is a sample deck of eight questions about Python, Git, Docker, Linux, and cloud basics.

**requirements.txt** lists pytest, the only library the project needs.

## Design choices

I kept the input and output in `main()` and `quiz()`, and put the logic in small functions that take arguments and return values. This makes them easy to test without typing answers by hand, which is why the tests are simple.

I chose CSV for the decks because anyone can edit it in a text editor or a spreadsheet, so adding new cards doesn't require touching the code.

Answers are matched exactly after ignoring case and spaces. That keeps the checking predictable, but it means answers in a deck should be short and specific, such as a command name or a single term, rather than a full sentence.

The retry round tracks missed cards by their question text and reuses `quiz()`, so the same code runs both rounds. I limited it to one retry round to keep the program simple, though it could be extended to repeat until every card is answered correctly.
