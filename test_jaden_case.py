"""Test jaden case."""
import pytest
from jaden_case import toJadenCase

quote = "How can mirrors be real if our eyes aren't real"
jquote = "How Can Mirrors Be Real If Our Eyes Aren't Real"


def test_case_1():
    assert toJadenCase(quote) == jquote


def test_case_empty():
    assert toJadenCase('') == ''
