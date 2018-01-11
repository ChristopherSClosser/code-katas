"""
Take debugging to a whole new level.

Given a string, remove every single bug.

This means you must remove all instances of the word 'bug'
from within a given string, unless the word is plural ('bugs').

import re
def debug(s):
    return re.sub(re.compile('bug(?!s)'), '', s)
"""


def debug(text):
    """Given a string, remove every single bug."""
    res = text[:]
    bug_idx = [
        i for i in range(len(text)) if text.startswith('bug', i)
    ]
    bugs_idx = [
        i for i in range(len(text)) if text.startswith('bugs', i)
    ]
    if not bug_idx:
        return res
    if bug_idx and not bugs_idx:
        res = res.replace('bug', '')
        return res
    for idx in bugs_idx:
        bug_idx.remove(idx)
    if bug_idx:
        res = res[:bug_idx[0]] + res[bug_idx[0] + 3:]
        return debug(res)
    return res


if __name__ == '__main__':  # pragma no cover
    print(debug(''))
