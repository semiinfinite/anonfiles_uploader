#!/usr/bin/python

import os
import sh
import sys

for dirname, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in filenames:
        toZip = os.path.join(dirname, filename)
        sh.zip(toZip, toZip)
