"""Test smallest int."""
import sys
import pytest
from smallest_int import findSmallestInt


def test_case_1():
    """test_case_1."""
    assert findSmallestInt([78, 56, 232, 12, 11, 43]) == 11


def test_case_2():
    """test_case_2."""
    assert findSmallestInt([78, 56, -2, 12, 8, -33]) == -33


def test_case_3():
    """test_case_3."""
    # assert findSmallestInt([0, -1 - sys.maxint, sys.maxint]) == -1 - sys.maxint


def test_case_fail():
    """test_case_fail."""
    with pytest.raises(Exception):
        findSmallestInt()
