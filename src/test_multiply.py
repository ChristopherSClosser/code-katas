"""Test multiply function."""
import pytest
from multiply import multiply


def test_case_1():
    """Test_case_1."""
    assert multiply(2, 2) == 4, 'expect 2x2 is 4'


def test_case_2():
    """Test_case_2."""
    assert multiply(2, 2) != 3, '2x2 not 3'


def test_case_3():
    """Test_case_3."""
    assert multiply(3, 3) == 9, 'expect 3x3 is 9'


def test_case_4():
    """Test_case_4."""
    assert multiply(1, 2) == 2


def test_case_fail():
    """test_case_fail."""
    with pytest.raises(Exception):
        multiply()
