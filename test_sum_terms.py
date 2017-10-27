"""Test sum of nth terms."""
import pytest
from sum_terms import series_sum


def test_case_1():
    """Test_case_1."""
    assert series_sum(1) == "1.00"


def test_case_2():
    """Test_case_2."""
    assert series_sum(2) == "1.25"


def test_case_3():
    """Test_case_3."""
    assert series_sum(3) == "1.39"


def test_case_4():
    """Test_case_4."""
    assert series_sum(4) == "1.49"


def test_case_5():
    """Test_case_5."""
    assert series_sum(5) == "1.57"


def test_case_6():
    """Test_case_6."""
    assert series_sum(6) == "1.63"


def test_case_7():
    """Test_case_7."""
    assert series_sum(7) == "1.68"


def test_case_fail():
    """test_case_fail."""
    with pytest.raises(Exception):
        series_sum()
