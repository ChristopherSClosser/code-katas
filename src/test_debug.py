"""Test debug."""

import pytest
import random
import string
from debug import debug


def real(s):
    """Return correct string for testing."""
    import re
    return re.sub(re.compile('bug(?!s)'), '', s)


def test_case_1():
    """."""
    assert debug('obugobugobuoobugsoo') == 'ooobuoobugsoo'


def test_case_2():
    """."""
    assert debug('obbugugo') == 'obugo'


def test_case_3():
    """."""
    assert debug('bugs bunny') == 'bugs bunny'


def test_case_4():
    """."""
    assert debug('bugs buggy') == 'bugs gy'


def test_case_5():
    """."""
    assert debug(
        'oaiwjefbugoijoijapsbugsdoibugbugjfoijasdfbugsbug'
    ) == 'oaiwjefoijoijapsbugsdoijfoijasdfbugs'


def test_case_6():
    """."""
    assert debug(
        'bugbugbugiahweoifuhiaasnoidfhnbugbugs'
    ) == 'iahweoifuhiaasnoidfhnbugs'


def test_case_7():
    """."""
    assert debug(
        'bugsbugswaoeifhiauwehfoiwubugshefjnviouah'
    ) == 'bugsbugswaoeifhiauwehfoiwubugshefjnviouah'


def test_case_8():
    """."""
    assert debug('bugbugbugbug') == ''


def test_case_9():
    """."""
    assert debug('bugsbugsbugsbugs') == 'bugsbugsbugsbugs'


def test_case_10():
    """."""
    assert debug('buggybugs') == 'gybugs'


def test_case_11():
    """."""
    assert debug(
        'oaisjdfowjefpoibugsjsofijeo oi bugs o bug f bug poaj sfd s'
    ) == 'oaisjdfowjefpoibugsjsofijeo oi bugs o  f  poaj sfd s'


@pytest.mark.parametrize('text', [i for i in range(100)])
def test_multi_random(text):
    """."""
    bugs = [' bug ', ' bugs ']
    rand = random.randint(0, 20)
    rand_input = ''.join([
        random.choice(
            string.ascii_lowercase + string.digits
        ) for _ in range(random.randint(1, 100))
    ])
    for _ in range(rand):
        length = len(rand_input)
        rand_idx = random.randint(0, length)
        rand_input = rand_input[
            :rand_idx
        ] + random.choice(bugs) + rand_input[rand_idx:]
    assert real(rand_input) == debug(rand_input)
