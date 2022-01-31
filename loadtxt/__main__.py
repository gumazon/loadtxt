#!/usr/bin/env python

import sys
from loadtxt import new


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            print(new(sys.argv[1]))
        except Exception as e:
            print(' '.join([str(_e) for _e in e.args]))
    else:
        print(new.__doc__)
