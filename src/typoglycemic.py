"""
Messes up the inner spelling of words.

To test this theory:
https://en.wikipedia.org/wiki/Typoglycemia
It's a lot harder to read than the exapmles online...

---------best practice--------
def scramble_words(words):
    import re
    new_words = []
    for word in words.split():
        begin, word = re.match(r"([-',.]*[a-zA-Z]?)(.*)", word).groups()
        word, end = re.match(
            r"(.*?)([a-zA-Z]?[-',.]*)$", word
        ).groups() if word else ("", "")
        sorted_word = list(sorted(c for c in word if c.isalpha()))
        for i, c in enumerate(word):
            if c in "-',.":
                sorted_word.insert(i, c)
        new_words.append(begin + "".join(sorted_word) + end)
    return " ".join(new_words)
"""


def messup(words):
    """Return string of words with the middle letters in alphabetical order."""
    res = ''
    sub = ''
    word = ''
    hold = None
    dash = None

    for char in words + ' ':
        if char.isalpha():
            sub += char
        elif char == '-' or char == "'" and len(sub) > 0:
            hold = len(sub)
            dash = char
        else:
            if len(sub) >= 3:
                word += sub[0]
                word += ''.join(sorted(sub[1:-1]))
                word += sub[-1]
                if dash:
                    word = word[:hold] + dash + word[hold:]
                res += word
            else:
                res += sub
            sub = ''
            word = ''
            dash = None
            hold = None
            res += char
    return res[:-1]


if __name__ == '__main__':  # pragma no cover
    print(messup(
        "you've gotta dance like there's nobody watching, \
        love like you'll never be hurt, sing like there's \
        nobody listening, and live like it's heaven on earth."
    ))
