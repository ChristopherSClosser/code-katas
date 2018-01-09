"""Test disemvowel."""
import pytest
from disemvowel import disemvowel


def test_case_1():
    """test_case_1."""
    assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"


def test_case_2():
    """test_case_2."""
    assert disemvowel("AEIOU This website is for losers LOL!") == " Ths wbst s fr lsrs LL!"


def test_case_empty():
    """test_case_empty."""
    assert disemvowel("aeiou") == ""


def test_case_fail():
    """test_case_fail."""
    with pytest.raises(Exception):
        disemvowel()
