"""Test Grasshopper."""
from grasshopper import move


def test_case_1():
    """test_case_1."""
    assert move(0, 4) == 8


def test_case_2():
    """test_case_2."""
    assert move(3, 6) == 15


def test_case_3():
    """test_case_3."""
    assert move(2, 5) == 12
