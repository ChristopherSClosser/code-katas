"""Test sort cards."""
import pytest
from sort_cards import sort_cards
from random import shuffle

sorted_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']


def test_sort_works():
    """Test first sort."""
    assert sort_cards(list('39A5T824Q7J6K')) == sorted_deck


def test_sort_works_2():
    """Test second sort."""
    assert sort_cards(list('Q286JK395A47T')) == sorted_deck


def test_sort_works_3():
    """Test third sort."""
    assert sort_cards(list('54TQKJ69327A8')) == sorted_deck


@pytest.mark.parametrize('cards', [i for i in range(80)])
def test_proper_sorting(cards):
    """Test sorting."""
    res = sorted_deck[:]
    shuffle(res)
    assert sort_cards(res) == sorted_deck
