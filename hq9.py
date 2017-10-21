r"""Kata: HQ9+.

Implement a simple interpreter for the notorious esoteric language HQ9+,
that will work for a single character input:

If the input is 'H', return 'Hello World!'
If the input is 'Q', return the input
If the input is '9', return the full lyrics of 99 Bottles of Beer.

- **URL**: [challenge url]
(https://www.codewars.com/kata/8kyu-interpreters-hq9-plus)

#1 Best Practices Solution by Chris_Rands

def HQ9(code):
    return {'H': 'Hello World!',
    'Q': 'Q',
    '9': ''.join(('{} bottle{} of beer on the wall, {} bottle{} of beer.\n'
    'Take one down and pass it around, {} bottle{} of beer on the wall.\n'
    ).format(i,'s'[i==1:], i,'s'[i==1:],[i-1,'no more'][i-1==0],'s'[i-1==1:])
    for i in range(99,0,-1)).strip()}.get(code,None)
"""


def HQ9(code):
    """Main function."""
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9' or code == 9:
        song = beer_song()
        return song
    else:
        return 'Wrong input!'


def beer_song():
    """Return all lyics."""
    lyr_a, lyr_b, lyr_c, lyr_d, lyr_e, lyr_f, lyr_g = (
        'bottles of beer on the wall, ',
        'bottles of beer.\n',
        'Take one down and pass it around, ',
        'bottles of beer on the wall.\n',
        'Take one down and pass it around, 1 bottle of beer on the wall.\n',
        '1 bottle of beer on the wall, 1 bottle of beer.\n',
        'Take one down and pass it around, no more bottles of beer on the wall.')
    bottles = 99
    song = ''
    for i in range(99, 0, -1):
        lyrics_1 = '{0} {1}{0} {2}'.format(bottles, lyr_a, lyr_b)
        song += lyrics_1
        bottles -= 1
        if bottles == 1:
            song += lyr_e + lyr_f + lyr_g
            break
        lyrics_2 = '{1}{0} {2}'.format(bottles, lyr_c, lyr_d)
        song += lyrics_2
    print(song)
    return song
