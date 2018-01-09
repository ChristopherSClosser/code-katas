"""Valid Parentheses.

Write a function that takes a string of parentheses,
and determines if the order of the parentheses is valid.
The function should return true if the string is valid,
and false if it's invalid.

- **URL**: [challenge url](https://www.codewars.com/kata/valid-parentheses/train/python)

#1 Best Practices Solution by albarralnunez & others
"""


def valid_parentheses(string):
    """Return True if all brackets match, False otherwise."""
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []

    for i in string:
        if i in open_list:
            stack.append(i)

        elif i in close_list:
            pos = close_list.index(i)

            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True

    return False
