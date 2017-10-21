"""Kata: Tribonacci.

Summing the last 3 numbers of a sequence to generate the next.

- **URL**: [challenge url](https://www.codewars.com/kata/tribonacci-sequence)

#1 Best Practices Solution by Abhi_Scorp & others

def tribonacci(signature,n):
    res = signature[:n]
    for i in range (n - 3): res.append(sum(res[-3:]))
    return res
"""


def tribonacci(signature, n):
    """Tribonacci sequence function."""
    results = signature
    if n < 3:
        new_res = []
        for i in range(n):
            new_res.append(signature[i])
        return new_res
    for i in range(0, n - 3):
        results.append(results[i] + results[i + 1] + results[i + 2])
    return results
