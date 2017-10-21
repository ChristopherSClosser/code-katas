"""Kata: Find the divisors.

takes an integer and returns an array with all of the integer's divisors
(except for 1 and the number itself).

- **URL**: [challenge url](https://www.codewars.com/kata/find-the-divisors)

#1 Best Practices Solution by BrookShuihuaLee & others

def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n
"""


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True


def divisors(n):
    if is_prime(n):
        return '%i is prime' % n
    div_l = [i for i in range(1, n + 1) if n % i == 0]
    if n in div_l:
        div_l.remove(n)
    if 1 in div_l:
        div_l.remove(1)
    print(div_l)
    return div_l
