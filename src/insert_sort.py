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

    def __init__(self, data):
        """."""
        self.data = data
        self.next = None


def insert_sort(head):
    """Linked list insert sort, return head of list."""
    if not head:
        return head
    comp, comp.next, curr = Node(0), head, head
    while curr:
        if curr.next and curr.next.data < curr.data:
            pre = comp
            while pre.next and pre.next.data < curr.next.data:
                pre = pre.next
            hold = pre.next
            pre.next = curr.next
            curr.next = curr.next.next
            pre.next.next = hold
        else:
            curr = curr.next
    return comp.next
