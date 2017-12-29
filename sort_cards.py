"""Sort shuffled list of cards, sorted by rank.

>>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

- **URL**: [challenge url](https://www.codewars.com/kata/sort-deck-of-cards/train/python)

#1 Best Practices Solution by zebulan & others
"""


def sort_cards(cards):
    """Return a list of sorted cards."""
    priority_q = PriorityQ()
    face_cards = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    for card in cards:
        try:
            deck_priority = int(card)
        except ValueError:
            deck_priority = face_cards[card]
        priority_q.insert(card, priority=deck_priority)
    return [card for priority, card in priority_q._list]


class PriorityQ(object):
    """Define atributes and methods of a PriorityQ."""

    def __init__(self):
        """Initialize."""
        self._list = []

    def insert(self, val, priority=None):
        """Add a value to the PQ."""
        new_item = [priority, val]
        if new_item[0] is None and self._list:
            new_item[0] = self._list[-1][0]
        if new_item[0] is None:
            new_item[0] = 0
        if type(new_item[0]) not in (int, float):
            raise ValueError('Please enter a number for priority.')
        if len(self._list) == 0:
            self._list.append(new_item)
            return
        for i in range(len(self._list)):
            if self._list[i][0] > new_item[0]:
                self._list.insert(i, new_item)
                return
        self._list.append(new_item)
