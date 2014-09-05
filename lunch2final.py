#!/usr/bin/env python
#Day 2 - Lunch

# Initialize variables
f = open("accepted_hits.sam")
genome_index = "/Users/cmdb/data/genomes/dmel-all-chromosome-5.57"

# 1. Find number of alignments

nl = 0
while True:
    line = f.readline()
    if line == "":
        break
    elif  "SRR" in line:
        nl = nl + 1
print nl
#total number of alignments = 18,417,196

# 2. Find number of perfect matches
nl = 0
while True:
    line = f.readline()
    if line == "":
        break
    elif  "HI:i:0" in line:
        nl = nl + 1
print nl
#number of perfect matches = 229,352


# 3. Find number of single-location matches
nl = 0
while True:
    line = f.readline()
    if line == "":
        break
    elif  "NH:i:1" in line:
        nl = nl + 1
print nl
# 17444398

#4
nl = 0
while True:
    line = f.readline()
    if line == "":
        break
    else:
        line.rstrip("r\n").split("\t")
print fields[2]