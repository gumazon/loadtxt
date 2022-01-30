#!/usr/bin/env python

import sys
from . import new


if __name__ == '__main__':
    try:
        print(new(sys.argv[1]))
    except Exception as e:
        print(' '.join([str(_e) for _e in e.args]))
