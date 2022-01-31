import re


def new(value=''):
    """
    Load text from file or string.


    Examples
    --------
    >>> new(value="temp/text.txt")

    :param value: <str> could be a text or a path to text file.

    :return: <str> Text from input or file.
    """
    path_pattern = r'^(([a-zA-Z]:)|((\\|/){1,2}\w+)\$?)((\\|/)(\w[\w ]*.*))+\.([a-zA-Z0-9]+)$'
    _output = ''
    f = ''
    v = ''
    if value:
        if not re.match(path_pattern, value):
            v = value
        else:
            f = value

    if f:
        with open(f, "r") as infile:
            _output = infile.read()
    else:
        _output = v

    return _output


