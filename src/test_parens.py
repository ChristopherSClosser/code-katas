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


PARENS = ["[", "{", "(", "]", ")"]
parens = ['()', '[]']
chars = 'abcdefghijklmnopqrstuvwxyz'


@pytest.mark.parametrize('times', [i for i in range(20)])
def test_false_random_sorts(times):
    """."""
    res = PARENS[:]
    random.shuffle(res)
    assert vp(str(res)) is False


@pytest.mark.parametrize('times', [i for i in range(20)])
def test_true_random_sorts(times):
    """."""
    res = parens[:]
    for i in range(20):
        res.append(random.choice(chars))
    random.shuffle(res)
    assert vp(str(res)) is True
