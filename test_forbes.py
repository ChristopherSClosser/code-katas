"""Test function for forbes module."""

import pytest
from calc_forbes import youngest_oldest as yo
from forbes_listing import FORBES, MOCK_FORBES


@pytest.fixture
def forbes():
    """Return dict of oldest and youngest billionaire."""
    return yo(FORBES)


@pytest.fixture
def mock_forbes():
    """Return mock dict for testing function."""
    return yo(MOCK_FORBES)


def test_forbes_returns_dict_with_oldest_youngest_keys(forbes):
    """test_forbes_returns_dict_with_oldest_youngest_keys."""
    res = list(forbes.keys())
    res.sort()
    assert res == ['oldest', 'youngest']


def test_forbes_returns_correct_youngest_name(forbes):
    """test_forbes_returns_correct_youngest_name."""
    assert forbes['youngest']['name'] == 'Mark Zuckerberg'


def test_forbes_returns_correct_youngest_assets(forbes):
    """test_forbes_returns_correct_youngest_name."""
    assert forbes['youngest']['net_worth (USD)'] == 44600000000


def test_forbes_function_returns_correct_youngest_name(mock_forbes):
    """test_forbes_function_returns_correct_youngest_name."""
    assert mock_forbes['youngest']['name'] == 'Justin Case'


def test_forbes_function_returns_correct_oldest_name(mock_forbes):
    """test_forbes_function_returns_correct_oldest_name."""
    assert mock_forbes['oldest']['name'] == 'Ben Dover'


def test_forbes_returns_correct_oldest_name(forbes):
    """test_forbes_returns_correct_oldest_name."""
    assert forbes['oldest']['name'] == 'Phil Knight'


def test_forbes_returns_correct_oldest_assets(forbes):
    """test_forbes_returns_correct_oldest_name."""
    assert forbes['oldest']['net_worth (USD)'] == 24400000000


def test_forbes_returns_correct_youngest_source(forbes):
    """test_forbes_returns_correct_youngest_source."""
    assert forbes['youngest']['source'] == 'Facebook'


def test_forbes_returns_correct_oldest_source(forbes):
    """test_forbes_returns_correct_oldest_source."""
    assert forbes['oldest']['source'] == 'Nike'


def test_forbes_returns_correct_oldest_age(forbes):
    """test_forbes_returns_correct_oldest_age."""
    assert forbes['oldest']['age'] == 78


def test_forbes_returns_correct_youngest_age(forbes):
    """test_forbes_returns_correct_youngest_age."""
    assert forbes['youngest']['age'] == 32
