"""Test insert sort."""

import pytest
import random
from insert_sort import LinkedList, insert_sort, display


TEST_WORDS = ['unwieldier', 'Quixote', 'illegalities', 'glands', 'pronoun',
              "bloodsucker's", 'jinni', 'belaying', 'Eve', 'dearly',
              'cloudier', 'tackle', "vein's", "multiplication's", 'entangles',
              "aftercare's", "literacy's", "childbearing's", 'Opal',
              'Inquisition', 'condescending', 'greying', "burden's", 'Lewis',
              'studying', 'sportscasts', 'explanatory', "minuteness's", 'Baku',
              'turbid', 'cogitation', "hairpin's", 'disappearances',
              "bathhouse's", 'delimiter', 'entrails', 'Chaplin', 'wigwagging',
              'hardiness', 'tome', 'humble', 'tubs', 'industrialist',
              "procrastinator's", "cornball's", "rubella's", 'Ngaliema',
              "now's", "Gatling's", 'mind']


@pytest.mark.parametrize('times', [y for y in range(0, 20)])
def test_insert_sort_orders_properly(times):
    """Test_insert_sort_orders_properly."""
    nums = random.sample(range(100), random.randint(0, 100))
    l_l = LinkedList(nums)
    assert display(insert_sort(l_l)) == sorted(nums)


@pytest.mark.parametrize('nums', [[random.uniform(-100, 100)
                                  for _ in range(y)]
                                  for y in range(0, 20)])
def test_insert_sort_with_floats(nums):
    """Test_insert_sort_with_floats."""
    l_l = LinkedList(nums)
    assert display(insert_sort(l_l)) == sorted(nums)


@pytest.mark.parametrize('words', [random.sample(TEST_WORDS, y)
                                   for y in range(0, 20)])
def test_insert_sort_words(words):
    """Test insertion sort works with words."""
    l_l = LinkedList(words)
    assert display(insert_sort(l_l)) == sorted(words)


def test_insert_sort_does_not_mutate_the_original_list():
    """Test_insert_sort_does_not_mutate_the_original_list."""
    t_l = [5, 2, 7, 4, 1]
    l_l = LinkedList(t_l)
    s_l = display(insert_sort(l_l))
    assert s_l is not t_l


def test_insert_sort_with_empty_list():
    """."""
    l_l = LinkedList()
    res = insert_sort(l_l)
    assert res is None
