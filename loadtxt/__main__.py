#!/usr/bin/env python
import re
import sys


def loadtxt(value):
    """
    Load text from file or string.


    Examples
    --------
    >>> loadtxt(value="temp/text.txt")

    :param value: <str> could be a text or a path to text file.

    :return: <str> Text from input or file.
    """

    if re.match(r'^(([a-zA-Z]:)|((\\|/){1,2}\w+)\$?)((\\|/)(\w[\w ]*.*))+\.([a-zA-Z0-9]+)$', value):
        with open(value, "r") as infile:
            return infile.read()
    else:
        return value



if __name__ == '__main__':
    print(loadtxt((sys.ps1 or '')))
