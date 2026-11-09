import pytest

from project import load_cards, check_answer, calculate_score, pick_weak_cards


def test_load_cards(tmp_path):
    file = tmp_path / "cards.csv"
    file.write_text("Capital of France?,Paris\n\n  Largest planet? , Jupiter \nBadRowNoAnswer\n")
    assert load_cards(file) == [
        ("Capital of France?", "Paris"),
        ("Largest planet?", "Jupiter"),
    ]

    with pytest.raises(FileNotFoundError):
        load_cards("does_not_exist.csv")


def test_check_answer():
    assert check_answer("paris", "Paris") is True
    assert check_answer("  PARIS  ", "Paris") is True
    assert check_answer("london", "Paris") is False
    assert check_answer("", "Paris") is False


def test_calculate_score():
    assert calculate_score(3, 4) == 75.0
    assert calculate_score(0, 5) == 0.0
    assert calculate_score(5, 5) == 100.0
    assert calculate_score(0, 0) == 0.0


def test_pick_weak_cards():
    cards = [("Q1", "A1"), ("Q2", "A2"), ("Q3", "A3")]
    assert pick_weak_cards(cards, ["Q2"]) == [("Q2", "A2")]
    assert pick_weak_cards(cards, ["Q1", "Q3"]) == [("Q1", "A1"), ("Q3", "A3")]
    assert pick_weak_cards(cards, []) == []