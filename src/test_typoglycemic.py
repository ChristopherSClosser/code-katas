"""Test Typoglycemia."""

import pytest
from faker import Faker
from typoglycemic import messup


def real(words):
    """."""
    import re
    new_words = []
    for word in words.split():
        begin, word = re.match(r"([-',.]*[a-zA-Z]?)(.*)", word).groups()
        word, end = re.match(
            r"(.*?)([a-zA-Z]?[-',.]*)$", word
        ).groups() if word else ("", "")
        sorted_word = list(sorted(c for c in word if c.isalpha()))
        for i, c in enumerate(word):
            if c in "-',.":
                sorted_word.insert(i, c)
        new_words.append(begin + "".join(sorted_word) + end)
    return " ".join(new_words)


def test_case_1():
    """."""
    assert messup('professionals') == 'paefilnoorsss'


def test_case_2():
    """."""
    assert messup('i') == 'i'


def test_case_3():
    """."""
    assert messup('') == ''


def test_case_4():
    """."""
    assert messup('me') == 'me'


def test_case_5():
    """."""
    assert messup('you') == 'you'


def test_case_6():
    """."""
    assert messup('card-carrying') == 'caac-dinrrryg'


def test_case_7():
    """."""
    assert messup("shan't") == "sahn't"


def test_case_8():
    """."""
    assert messup('-dcba') == '-dbca'


def test_case_9():
    """."""
    assert messup('dcba.') == 'dbca.'


def test_case_10():
    """."""
    assert messup(
        "you've gotta dance like there's nobody watching, \
        love like you'll never be hurt, sing like there's nobody listening, \
        and live like it's heaven on earth."
    ) == "you've gotta dacne like teehr's nbdooy wachintg, \
        love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, \
        and live like it's haeevn on earth."


@pytest.mark.parametrize('text', [_ for _ in range(50)])
def test_multi_random(text):
    """."""
    rand_input = Faker().paragraph()
    assert real(rand_input) == messup(rand_input)
