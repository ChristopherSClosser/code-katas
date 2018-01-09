"""
String incrementer.

my favorite...
def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))

    return s + "1"
"""
import re

strng = 'sklasdfjioweu2'


def increment_string(s):
    """
    Your job is to write a function which increments a string.

    To create a new string. If the string already ends with a number,
    the number should be incremented by 1. If the string does not end
    with a number the number 1 should be appended to the new string.
    """
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))

    return s + "1"
    # try:
    #     strnum = re.compile(r'(\d+)$').search(strng).group(1)
    # except:
    #     strnum = ''
    # if strnum:
    #     num = int(strnum) + 1
    # else:
    #     num = 1
    #     res = strng + str(num).zfill(len(strnum))
    #     return res
    # try:
    #     res = strng.replace(strnum, str(num).zfill(len(strnum)))
    # except:
    #     return res
    # return res


if __name__ == '__main__':
    print(increment_string(strng))
