"""Test parentheses mathcher."""

import pytest

import random

from proper_parenthetics import valid_parentheses as vp


def test_case_1():
    """."""
    assert vp(' (') is False


def test_case_2():
    """."""
    assert vp(")test") is False


def test_case_3():
    """."""
    assert vp("") is True


def test_case_4():
    """."""
    assert vp("hi(hi)()") is True


def test_case_5():
    """."""
    assert vp("hi())(") is False
# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)
