import re

import sys


def load(data='/Users/smikhail/Public/wordcountz/wordcountz/temp/jeffrey_epstein.txt'):
    """Load text from a text file and return as a string.

Parameters
----------
data: str
    could be a file or text.

    file : path
        Path to text file. <matches path pattern: r'^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))'>

    text : str
        Text string.

Returns
-------
str
    Text from text input or file.

Examples
--------
>>> load(data="temp/text.txt")

"""

    path_pattern = r'^(.*/)?(?:$|(.+?)(?:(\.[^.]*$)|$))'

    if data:
        if re.match(path_pattern, data):
            with open(data, "r") as infile:
                return infile.read()
        else:
            return data


if __name__ == '__main__':
    try:
        print(load(sys.argv[1]))
    except Exception as e:
        print(' '.join([_earg for _earg in e.args[0:]]))
