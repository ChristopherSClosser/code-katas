"""You have to build a pyramid.

This pyramid should be built from characters from a given string.

You have to create the code for these four methods:

watch_pyramid_from_the_side(characters):

watch_pyramid_from_above(characters):

count_visible_characters_of_the_pyramid(characters):

count_all_characters_of_the_pyramid(characters):
The first method ("FromTheSide") shows the pyramid as you would see from the side.
The second method ("FromAbove") shows the pyramid as you would see from above.
The third method ("CountVisibleCharacters") should return the count of all characters, that are visible from outside the pyramid.
The forth method ("CountAllCharacters") should count all characters of the pyramid. Consider that the pyramid is completely solid and has no holes or rooms in it.

Every character will be used for building one layer of the pyramid. So the length of the given string will be the height of the pyramid. Every layer will be built with stones from the given character. There is no limit of stones.
The pyramid should have perfect angles of 45 degrees.

- **URL**: [challenge url](https://www.codewars.com/kata/string-pyramid/train/python)

#1 Best Practices Solution by Blind4Basics
"""


def watch_pyramid_from_the_side(characters):
    """Show the pyramid as you would see it from the side."""
    if not characters:
        return characters
    _len = len(characters)*2-1
    res = '\n'.join(' '*(i) + characters[i]*(_len-2*i) +
                    ' '*(i) for i in range(len(characters)-1, -1, -1))
    return res


def watch_pyramid_from_above(characters):
    """Show the pyramid as you would see from above."""
    if not characters:
        return characters
    _len = len(characters)*2-1
    res = '\n'.join(characters[0:min(i, _len-1-i)] +
                    characters[min(i, _len-1-i)]*(_len-2*min(i, _len-1-i)) +
                    characters[0:min(i, _len-1-i)][::-1] for i in range(_len))
    return res


def count_visible_characters_of_the_pyramid(characters):
    """Return the count of all characters, that are visible from outside the pyramid."""
    return -1 if not characters else (len(characters)*2-1)**2


def count_all_characters_of_the_pyramid(characters):
    """Count all characters of the pyramid.

    Consider that the pyramid is solid and has no holes or rooms in it.
    """
    return -1 if not characters else sum((2*i+1)**2 for i in range(len(characters)))
