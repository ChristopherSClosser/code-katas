"""Test find divisors."""
from find_divisors import divisors
from find_divisors import is_prime


def test_case_15():
    assert divisors(15) == [3, 5]


def test_case_12():
    assert divisors(12) == [2, 3, 4, 6]


def test_case_13():
    assert divisors(13) == '13 is prime'


def test_case_97():
    assert divisors(97) == '97 is prime'


def test_case_prime():
    assert is_prime(2) is True


def test_case_not_prime():
    assert is_prime(50) is False
