"""
Find all files in the current directory where you run your code.

then make a dictionary in the following manner.

{ filename : first line of the file , ...}.

look to write me for more advanced file reading...
"""


def create_file_dict():
    """Return a dictionary of file paths as key and first line as val."""
    import os
    file_dict = {}
    for root, dirs, files in os.walk('.'):
        dirs[:] = [  # add any extra dirs to ignore #
           d for d in dirs
           if '.' not in d
           and 'ENV' not in d
           and '__' not in d
           and 'build' not in d
        ]
        for f in files:
            try:
                with open(f, 'r') as thing:
                    res = thing.readline()
            except:
                res = ''
            file_name = os.path.join(root, f).lstrip('./')
            file_dict[file_name] = res
    return file_dict


if __name__ == '__main__':  # pragma no cover
    print(create_file_dict())
