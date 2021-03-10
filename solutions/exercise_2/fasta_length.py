#!/opt/conda/bin/python3

# Author: Katharina Hoff
# Matriculation Number: NA
# Study Program: Molecular Biology
# E-Mail: katharina.hoff@uni-greifswald.de
# Last modified on: April 28th 2020

# call this script with:
# cat sequences.fa | fasta_length.py

# insert code at places that contain capitalized comments (LIKE THIS)

import fileinput

len_dict = {}

for line in fileinput.input():
    if not line:
        continue
    else:
        line = line.strip()
        if line.startswith(">"):
            current_header = line
            len_dict[current_header] = 0
        else:
            len_dict[current_header] += len(line)

for seqname, length in len_dict.items():
    print("Length of sequence " + seqname + " is " + str(length))
