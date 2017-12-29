"""Test parentheses mathcher."""

import pytest

import random

from proper_parenthetics import valid_parentheses as vp


def test_case_1():
    """."""
    assert vp(' (') is False

# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)
