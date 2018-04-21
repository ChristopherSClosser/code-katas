"""."""


def camel_case(string):
    """Simple camel case fuction."""
    return ''.join(w.capitalize() for w in string.split())
