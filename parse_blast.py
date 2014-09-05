#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""

#to run this, type "./parse_one_blast.py < blastout | less -S"

import sys
from blast import BLASTReader

reader = BLASTReader(sys.stdin)
for sid, sequence in reader:
    #sid, sequence = reader.next() #used to be a while loop
    print sid, sequence