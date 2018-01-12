"""
Linked Lists - Insert Sort.

Write an InsertSort() function which rearranges nodes in a linked list so
they are sorted in increasing order. You can use the SortedInsert() function
that you created in the "Linked Lists - Sorted Insert" kata below.
The InsertSort() function takes the head of a linked list as an argument and
must return the head of the linked list.

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insert_sort(head):
    n, r = head, None
    while n:
        r = sorted_insert(r, n.data)
        n = n.next
    return r
"""


class Node(object):
    """Node object constructor."""

    def __init__(self, data, next=None):
        """."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Class for a linked list."""

    def __init__(self, iterable=None):
        """On list creation set head to none."""
        self.head = None
        self.length = 0
        if isinstance(iterable, (str, tuple, list)):
            for i in iterable:
                self.push(i)

    def push(self, data):
        """Push a val to the list."""
        self.head = Node(data, self.head)
        self.length += 1


def insert_sort(ll):
    """Linked list insert sort, return head of list."""
    count = 0
    comp, comp.next, curr = Node(0), ll.head, ll.head
    while curr:
        if curr.next and curr.next.data < curr.data:
            pre = comp
            while pre.next and pre.next.data < curr.next.data:
                pre = pre.next
                count += 1
            hold = pre.next
            pre.next = curr.next
            curr.next = curr.next.next
            pre.next.next = hold
        else:
            curr = curr.next
        count += 1
    return comp.next


def display(head):
    """."""
    res = []
    if not head:
        return res
    curr = head
    while curr:
        res.append(curr.data)
        curr = curr.next
    return res


if __name__ == '__main__':  # pragma no cover
    ll = LinkedList((2, 88, 52, 5, 47, 1, 66, 7, 99, 4, 23, 200, 31, 300))
    curr = insert_sort(ll)
    res = []
    while curr:
        res.append(curr.data)
        curr = curr.next
