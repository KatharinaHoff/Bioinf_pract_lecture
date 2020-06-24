#!/usr/bin/env python3

# Author: Katharina J. Hoff
# Matriculation Number: NA
# Study Program: NA
# E-Mail: katharina.hoff@uni-greifswald.de
# Last modified on Apr 16th 2018

# call this script with:
# cat numbers.lst | num_stats.pl

import fileinput
import numpy

numbers = []

for line in fileinput.input():
    if not line:
        continue
    else:
        line = line.strip()
        numbers.append(float(line))

print("The minimum is: " + str(min(numbers)))
print("The maximum is: " + str(max(numbers)))
print("The mean is: " + str(numpy.mean(numbers)))
