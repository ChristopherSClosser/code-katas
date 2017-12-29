"""Test string pyramid."""

import pytest

from unittest import TestCase

from string_pyramid import watch_pyramid_from_the_side, watch_pyramid_from_above, count_visible_characters_of_the_pyramid, count_all_characters_of_the_pyramid


def test_watch_from_side():
    """."""
    expected = ' # \n***'
    characters = '*#'
    actual = watch_pyramid_from_the_side(characters)
    assert expected == actual
    # def test_visualisation(self, expected_watch_from_side, expected_watch_from_above, actual_watch_from_side, actual_watch_from_above):
    #     print('From side correct:\n{}'.format(expected_watch_from_side))
    #     print('--------------------------------------')
    #     print('From above correct:\n{}'.format(expected_watch_from_above))
    #     print('--------------------------------------')
    #     print('From side yours:\n{}'.format(actual_watch_from_side))
    #     print('--------------------------------------')
    #     print('From above yours:\n{}'.format(actual_watch_from_above))
    #     self.assert_equals(actual_watch_from_side, expected_watch_from_side)
    #     self.assert_equals(actual_watch_from_above, expected_watch_from_above)
    #
    #     self.describe('Basic Tests')
    #
    #     self.it('should handle 2 characters')
    #     characters = '*#'
    #     expected_watch_from_side = ' # \n***'
    #     expected_watch_from_above = '***\n*#*\n***'
    #     actual_watch_from_side = watch_pyramid_from_the_side(characters)
    #     actual_watch_from_above = watch_pyramid_from_above(characters)
    #     test_visualisation(
    #         expected_watch_from_side, expected_watch_from_above,
    #         actual_watch_from_side, actual_watch_from_above
    #     )
    #     self.assert_equals(count_visible_characters_of_the_pyramid(characters), 9)
    #     self.assert_equals(count_all_characters_of_the_pyramid(characters), 10)
    #
    #     self.it('should handle 3 characters')
    #     characters = 'abc'
    #     expected_watch_from_side = '  c  \n bbb \naaaaa'
    #     expected_watch_from_above = '''\
    #     aaaaa
    #     abbba
    #     abcba
    #     abbba
    #     aaaaa'''
    #     actual_watch_from_side = watch_pyramid_from_the_side(characters)
    #     actual_watch_from_above = watch_pyramid_from_above(characters)
    #     test_visualisation(
    #         expected_watch_from_side, expected_watch_from_above,
    #         actual_watch_from_side, actual_watch_from_above
    #     )
    #     self.assert_equals(count_visible_characters_of_the_pyramid(characters), 25)
    #     self.assert_equals(count_all_characters_of_the_pyramid(characters), 35)
