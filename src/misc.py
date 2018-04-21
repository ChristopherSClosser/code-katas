"""."""


def camel_case(string):
    """Simple camel case fuction string with spaces."""
    return ''.join(w.capitalize() for w in string.split())


def to_camel_case(text):
    """Recursive deals with words seperated by dash and or underscore."""
    res = ''
    tmp = ''
    if '-' in text:
        tmp = text.split('-')
        res += tmp[0]
    elif '_' in text:
        tmp = text.split('_')
        res += tmp[0]
    if tmp:
        for word in tmp[1:]:
            word = word[0].capitalize() + word[1:]
            res += word
    if '-' in res or '_' in res:
        print(res)
        return to_camel_case(res)
    return res


def to_camel_case_better(s):
    """Same as above codewars #1 single liner."""
    return s[0] + s.title().translate(None, "-_")[1:] if s else s


def min_value(digits):
    """."""
    return int(''.join(map(str, sorted(set(digits)))))


ZEETALPH = {
    'A': '@', 'B': '8', 'C': '(', 'D': 'D',
    'E': '3', 'F': 'F', 'G': '6', 'H': '#',
    'I': '!', 'J': 'J', 'K': 'K', 'L': '1',
    'M': 'M', 'N': 'N', 'O': '0', 'P': 'P',
    'Q': 'Q', 'R': 'R', 'S': '$', 'T': '7',
    'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', 'Z': '2'
}


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


def dashatize(num):
    """."""
    import re
    return '-'.join(
        ' '.join(re.split(r'([13579])', str(abs(num)))).split()
    ) if num else '0' if num == 0 else 'None'
    """
        from random import randint
        import re

        # You can use Test.describe and Test.it to write BDD style test groupings
        test.describe('Basic')
        test.assert_equals(dashatize(274),"2-7-4", "Should return 2-7-4")
        test.assert_equals(dashatize(5311),"5-3-1-1", "Should return 5-3-1-1")
        test.assert_equals(dashatize(86320),"86-3-20", "Should return 86-3-20")
        test.assert_equals(dashatize(974302),"9-7-4-3-02", "Should return 9-7-4-3-02")
        test.describe('Weird')
        test.assert_equals(dashatize(None),"None", "Should return None");
        test.assert_equals(dashatize(0),"0", "Should return 0");
        test.assert_equals(dashatize(-1),"1", "Should return 1");
        test.assert_equals(dashatize(-28369),"28-3-6-9", "Should return 28-3-6-9");
        test.describe('Random')
        def mySolution(num):
            p = re.compile(r"([13579])")
            return p.sub('-\\1-',str(num)).replace('--','-').strip('-')
        for j in range(100):
            input = randint(0,999999999)
            test.assert_equals(dashatize(input), mySolution(input))
    """


def most_frequent_item_count(lst):
    return max([lst.count(lst[i]) for i in range(len(lst))]) if lst else 0


def sumDigits(number):
    return sum(map(int, list(str(abs(number)))))

    """
        test.assert_equals(sumDigits(10), 1)
        test.assert_equals(sumDigits(99), 18)
        test.assert_equals(sumDigits(-32), 5)
        test.assert_equals(sumDigits(1234567890), 45)
        test.assert_equals(sumDigits(0), 0)
        test.assert_equals(sumDigits(666), 18)
        test.assert_equals(sumDigits(100000002), 3)
        test.assert_equals(sumDigits(800000009), 17)
    """
