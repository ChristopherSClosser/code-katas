"""Test rotate matrix."""

import pytest
from rotate_matrix import rotate_in_place as rip
import random
from copy import deepcopy


def test_empty_matrix():
    """test_empty_matrix."""
    tm = []
    assert rip(tm) == []


def test_3_by_3():
    """Test rotation of a 3x3 matrix."""
    matrix_input = [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
    ]
    matrix_output = [
                     [7, 4, 1],
                     [8, 5, 2],
                     [9, 6, 3]
    ]
    assert rip(matrix_input) == matrix_output


@pytest.mark.parametrize('times', [i for i in range(10)])
def test_correct_rotation_4x4(times):
    """"test_correct_rotation."""
    tm = []
    for i in range(4):
        tm.append(random.sample(range(100), 4))
    comp = deepcopy(tm[0])
    res = rip(tm)
    comp2 = []
    for item in res:
        comp2.append(item[3])
    assert comp == comp2
