"""Test friend or foe."""
import pytest
from friend_foe import friend


def test_case_1():
    assert friend(["Ryan", "Kieran", "Mark"]) == ["Ryan", "Mark"]


def test_case_empty():
    assert friend([]) == []


def test_case_fail():
    with pytest.raises(Exception):
        friend()
