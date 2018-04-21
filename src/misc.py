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
