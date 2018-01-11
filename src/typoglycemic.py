"""
Messes up the inner spelling of words.

To test this theory:
https://en.wikipedia.org/wiki/Typoglycemia
It's a lot harder to read than the exapmles online...

---------best practice--------
def scramble_words(words):
    words = words.split()
    ans = []
    for w in words:
        l = [[w[i],i] for i in range(len(w)) if w[i] in "-',."]
        x = w.translate(None,"-',.")
        x = [x[0]] + sorted(x[1:-1]) + [x[-1]] if len(x) > 1 else x
        for c in l:
            x.insert(c[1],c[0])
        ans += [''.join(x)]
    return ' '.join(ans)
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


if __name__ == '__main__':
    print(messup("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."))

# Test.describe("Basic tests")
# Test.assert_equals(scramble_words('professionals'), 'paefilnoorsss', 'The first and last letters of a word should reamin in place with the inner letters sorted')
# Test.assert_equals(scramble_words('i'), 'i', 'Must handle single charater words')
# Test.assert_equals(scramble_words(''), '', 'Must handle empty strings')
# Test.assert_equals(scramble_words('me'), 'me', 'Must handle 2 charater words')
# Test.assert_equals(scramble_words('you'), 'you', 'Must handle 3 charater words')
# Test.assert_equals(scramble_words('card-carrying'), 'caac-dinrrryg', 'Only spaces separate words and punctuation should remain at the same place as it started')
# Test.assert_equals(scramble_words("shan't"), "sahn't", 'Punctuation should remain at the same place as it started')
# Test.assert_equals(scramble_words('-dcba'), '-dbca', 'Must handle special character at the start')
# Test.assert_equals(scramble_words('dcba.'), 'dbca.', 'Must handle special character at the end')
# Test.assert_equals(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."), "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.", 'Must handle a full sentence')
