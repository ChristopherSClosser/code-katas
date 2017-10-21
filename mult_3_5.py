"""Kata: Multiples of 3 and 5.

List all the natural numbers that are multiples of 3 or 5.

- **URL**: [challenge url](https://www.codewars.com/kata/multiples-of-3-and-5)

#1 Best Practices Solution by zyxwhut & others

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


def solution(num):
    """Run(s) nice and fast."""
    return sum(set(list(range(0, num, 3)) + list(range(0, num, 5))))
