#!/opt/conda/bin/python3

# Author: INSERT HERE
# Matriculation Number: INSERT HERE
# Study Program: INSERT HERE
# E-Mail: INSERT HERE
# Last modified on: INSERT HERE

# call this script with:
# cat sequences.fa | fasta_length.py

# insert code at places that contain capitalized comments (LIKE THIS)

import fileinput

len_dict = {}

for line in fileinput.input():
    if not line:
        continue
    else:
        # REMOVE TRAILING NEWLINE CHARACTER
        if # CHECK IF LINE STARTS WITH ">"
            current_header = line
            len_dict[current_header] = 0
        else:
            # ADD LENGTH OF CURRENT LINE TO len_dict[current_header]

for seqname, length in len_dict.items():
    print("Length of sequence " + seqname + " is " + str(length))
