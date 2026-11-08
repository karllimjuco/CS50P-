from datetime import date

import pytest

from seasons import minutes_lived, minutes_in_words


def test_minutes_lived_one_year():
    # 2001 is not a leap year, so this span is exactly 365 days.
    born = date(2001, 1, 1)
    today = date(2002, 1, 1)
    assert minutes_lived(born, today) == 365 * 24 * 60


def test_minutes_lived_zero():
    day = date(2020, 6, 15)
    assert minutes_lived(day, day) == 0


def test_minutes_in_words():
    # 2001->2002 is a non-leap 365-day span: 365 * 1440 = 525600 minutes.
    born = date(2001, 1, 1)
    today = date(2002, 1, 1)
    assert minutes_in_words(born, today) == (
        "Five hundred twenty-five thousand, six hundred minutes"
    )


def test_leap_year():
    born = date(2000, 1, 1)
    today = date(2000, 3, 1)
    # 2000 is a leap year: Jan (31) + Feb (29) = 60 days.
    assert minutes_lived(born, today) == 60 * 24 * 60