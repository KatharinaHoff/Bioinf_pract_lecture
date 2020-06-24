#!/opt/conda/bin/python3
from __future__ import print_function
# A future statement is a directive to the compiler that a
# particular module should be compiled using syntax or
# semantics that will be available in a specified future
# release of Python. The future statement is intended to ease
# migration to future versions of Python that introduce
# incompatible changes to the language. It allows use of the
# new features on a per-module basis before the release in
# which the feature becomes standard.

# call this script with:
# cat textfile | print_and_read.py

# Printing to STDOUT

print("This is printed to STDOUT")

# Printing to STDERR

"""eprint(str) print string to STDERR"""


def eprint(*args, **kwargs):
    import sys
    print(*args, file=sys.stderr, **kwargs)


eprint("This is printed to STDERR")

# Reading from STDIN (one of several options)

import fileinput
for line in fileinput.input():
    print(line)
