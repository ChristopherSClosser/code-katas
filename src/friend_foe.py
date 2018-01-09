"""Kata: Friend or foe.

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

- **URL**: [challenge url](https://www.codewars.com/kata/friend-or-foe)

#1 Best Practices Solution by SquishyStrawberry & others

def friend(x):
    return [f for f in x if len(f) == 4]
"""


def friend(names):
    result = []
    for name in names:
        if len(name) == 4:
            result.append(name)
    return result
