"""Test string pyramid."""

import pytest

from string_pyramid import (
    watch_pyramid_from_the_side,
    watch_pyramid_from_above,
    count_visible_characters_of_the_pyramid,
    count_all_characters_of_the_pyramid
)


@pytest.fixture
def characters():
    """."""
    return '*#'


@pytest.fixture
def more_chars():
    """."""
    return 'abc'


def test_watch_from_side(characters):
    """."""
    expected = ' # \n***'
    actual = watch_pyramid_from_the_side(characters)
    assert expected == actual


def test_watch_from_side_2(more_chars):
    """."""
    expected = '  c  \n bbb \naaaaa'
    actual = watch_pyramid_from_the_side(more_chars)
    assert expected == actual


def test_watch_from_above(characters):
    """."""
    expected = '***\n*#*\n***'
    actual = watch_pyramid_from_above(characters)
    assert expected == actual


def test_watch_from_above_2(more_chars):
    """."""
    expected = 'aaaaa\nabbba\nabcba\nabbba\naaaaa'
    actual = watch_pyramid_from_above(more_chars)
    assert expected == actual


def test_count_vivsible_characters(characters):
    """."""
    assert count_visible_characters_of_the_pyramid(characters) == 9


def test_count_vivsible_characters_2(more_chars):
    """."""
    assert count_visible_characters_of_the_pyramid(more_chars) == 25


def test_count_all_characters(characters):
    """."""
    assert count_all_characters_of_the_pyramid(characters) == 10


def test_count_all_characters_2(more_chars):
    """."""
    assert count_all_characters_of_the_pyramid(more_chars) == 35


def test_vivsible_characters_with_3():
    """."""
    assert count_visible_characters_of_the_pyramid('cba') == 25


def test_all_characters_with_3():
    """."""
    assert count_all_characters_of_the_pyramid('cba') == 35
