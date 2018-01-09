"""Kata: Find the smallest integer in the array.

Given an array of integers your solution should find the smallest integer.

- **URL**: [challenge url](https://www.codewars.com/kata/find-the-smallest-integer-in-the-array)

#1 Best Practices Solution by GNX & others

def findSmallestInt(arr):
    return min(arr)
"""


def findSmallestInt(arr):
    """First sort the list : return first item."""
    result = sorted(arr)
    return result[0]
