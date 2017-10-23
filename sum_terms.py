"""Kata: Sum of the first nth term of Series.

Your task is to write a function which returns the sum of following series upto nth term(parameter).

- **URL**: [challenge url](https://www.codewars.com/kata/sum-of-the-first-nth-term-of-series)

#1 Best Practices Solution by MMMAAANNN & others

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Sum of the first nth term of Series."""
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
