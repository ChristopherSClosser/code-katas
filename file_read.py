"""
Find all files in the current directory where you run your code.

then make a dictionary in the following manner.

{ filename : first line of the file , ...}.

look to write me for more advanced file reading...
"""


def create_file_dict():
    """."""
    import os
    file_dict = {}
    for root, dirs, files in os.walk("."):
        for f in files:
            with open(f, 'r') as thing:
                res = thing.readline()
            file_name = os.path.join(root, f)
            file_dict[file_name] = res


if __name__ == '__main__':
    create_file_dict()
