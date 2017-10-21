"""Kata: Jaden Casing Strings.

Convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

- **URL**: [challenge url](https://www.codewars.com/kata/jaden-casing-strings)

#1 Best Practices Solution by SquishyStrawberry & others

def friend(x):
    return [f for f in x if len(f) == 4]
"""


def toJadenCase(string):
    if not string:
        return ''
    return ' '.join(word[:1].upper() + word[1:] for word in string.split(' '))
