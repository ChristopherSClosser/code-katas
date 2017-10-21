"""Kata: Tribonacci.

Summing the last 3 numbers of a sequence to generate the next.

- **URL**: [challenge url](https://www.codewars.com/kata/tribonacci-sequence)

#1 Best Practices Solution by Abhi_Scorp & others

def tribonacci(signature,n):
    res = signature[:n]
    for i in range (n - 3): res.append(sum(res[-3:]))
    return res
"""


def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9' or code == 9:
        song = beer_song()
        return song


def beer_song():
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
