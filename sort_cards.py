"""Sort shuffled list of cards, sorted by rank.

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

"""


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank."""
    nums = sorted([i for i in cards if i.isdigit()])
    aces = [i for i in cards if i.upper() == 'A']
    tens = [i for i in cards if i.upper() == 'T']
    jacks = [i for i in cards if i.upper() == 'J']
    queens = [i for i in cards if i.upper() == 'Q']
    kings = [i for i in cards if i.upper() == 'K']

    res = aces + nums + tens + jacks + queens + kings
    return res
