"""Test string increment."""
import pytest
import random
import string
from string_increment import increment_string


def test_case_0():
    """test_case_0."""
    assert increment_string("foo") == "foo1"


def test_case_1():
    """test_case_1."""
    assert increment_string("foobar001") == "foobar002"


def test_case_2():
    """test_case_2."""
    assert increment_string("foobar1") == "foobar2"


def test_case_3():
    """test_case_3."""
    assert increment_string("foobar00") == "foobar01"


def test_case_4():
    """test_case_4."""
    assert increment_string("foobar99") == "foobar100"


def test_case_5():
    """test_case_5."""
    assert increment_string("") == "1"


def test_case_6():
    """test_case_6."""
    assert increment_string("foobar000") == "foobar001"


def test_case_7():
    """test_case_7."""
    assert increment_string("foobar999") == "foobar1000"


def test_case_8():
    """test_case_8."""
    assert increment_string("foobar00999") == "foobar01000"


def test_case_9():
    """test_case_9."""
    assert increment_string("foobar001") == "foobar002"


def test_case_10():
    """test_case_10."""
    assert increment_string("foobar1") == "foobar2"


def test_case_11():
    """test_case_11."""
    assert increment_string("1") == "2"


def test_case_12():
    """test_case_12."""
    assert increment_string("009") == "010"


def real(s):
    """Proper function from kata designer."""
    head = s.rstrip('0123456789')
    tail = s[len(head):]
    if tail == "":
        return s+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


@pytest.mark.parametrize('times', [i for i in range(200)])
def test_random(times):
    """."""
    _nums = random.sample(
        range(10),
        random.randint(1, 9)
    )
    _nums = ''.join(map(str, _nums))
    _input = ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(
            random.randint(0, 100)
        )
    ) + _nums
    _output = increment_string(_input)
    _real = real(_input)
    assert _output == _real
