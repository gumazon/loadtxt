#!/usr/bin/env python

import sys
from loadtxt import loadtxt

print(loadtxt((sys.argv[1] if len(sys.argv) > 1 else '')))
