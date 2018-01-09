"""Test tribonacci sequence."""
import pytest
from tribonacci import tribonacci


def test_case_111():
    """test_case_111."""
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]


def test_case_001():
    """test_case_001."""
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]


def test_case_011():
    """test_case_011."""
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]


def test_case_100():
    """test_case_100."""
    assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]


def test_case_000():
    """test_case_000."""
    assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_case_123():
    """test_case_123."""
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]


def test_case_321():
    """test_case_321."""
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]


def test_case_1112():
    """test_case_1112."""
    assert tribonacci([1, 1, 1], 2) == [1, 1]


def test_case_0():
    """test_case_0."""
    assert tribonacci([300, 200, 100], 0) == []


def test_case_half():
    """test_case_half."""
    assert tribonacci([0.5, 0.5, 0.5], 30) == [
        0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5,
        177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5,
        23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5,
        1655616.5, 3045153.5, 5600910.5, 10301680.5
    ]


def test_case_fail1():
    """test_case_fail1."""
    with pytest.raises(Exception):
        tribonacci([1, 2, 3])


def test_case_fail2():
    """test_case_fail2."""
    with pytest.raises(Exception):
        tribonacci(5)
