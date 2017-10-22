"""Kata: Disemvowel Trolls.

Your task is to write a function that takes a string and return a new string with all vowels removed.

- **URL**: [challenge url](https://www.codewars.com/kata/disemvowel-trolls)

#1 Best Practices Solution by Azuaron & others

def toJadenCase(string):
    return " ".join(w.capitalize() for w in string.split())
"""


def disemvowel(text):
    """Remove vowels from a string."""
    word = ""
    vowels = "ieaouIEAOU"
    for char in text:
        for v in vowels:
            if char == v:
                char = ""
            else:
                char = char
        word += char
    return word
