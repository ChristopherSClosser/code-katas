"""Test multiples of 3 and 5."""
from mult_3_5 import solution
import pytest


def test_case_10():
    assert solution(10) == 23


def test_case_100():
    assert solution(100) == 2318


def test_case_100():
    assert solution(0) == 0


def test_case_fail():
    with pytest.raises(Exception):
        solution()


def test_case_failfloat():
    with pytest.raises(Exception):
        solution(0.5)
