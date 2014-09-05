#!/usr/bin/env python
"""
EXERCISE
	for sample SRR..893
	determine GC content of 500 bp region around each transcription start site
	build linear regression model of FPKM~GC (maybe take log)
	plot with regression line
	(hints)
	can accomplish several tasks easily
	use grep, awk, fedtools, python
"""

# Pull transcripts.gtf
#in Terminal:
# awk '$3 =="transcript"' transcripts.gtf | grep "-" > minus_transcripts.txt
# awk '$3 =="transcript"' transcripts.gtf | grep "+" > plus_transcripts.txt

#ALTERNATE METHOD: grep "transcript\t" transcripts.gtf > transcripts_no_exons.gtf


# bedtools flank -l 250 -r 0 -i plus_transcripts.gtf -g genome_sized.txt  > bed_out_plus_1.gtf
# bedtools slop -l 0 -r 250 -i bed_out_plus_1.gtf -g genome_sized.txt  > bed_out_plus_2.gtf
# bedtools getfasta -fi dmel-all-chromosome-r5.57.fa -bed bed_out_plus_2.gtf -fo bed_out_plus.fasta


# bedtools flank -r 250 -l 0 -i minus_transcripts.gtf -g genome_sized.txt  > bed_out_minus_1.gtf
# bedtools slop -r 0 -l 250 -i bed_out_minus_1.gtf -g genome_sized.txt  > bed_out_minus_2.gtf
# bedtools getfasta -s -fi dmel-all-chromosome-r5.57.fa -bed bed_out_minus_2.gtf -fo bed_out_minus.fasta





#less -S filename


# Calculate GC content
# ./day4lunch.py input.fasta



# Calculate GC content
import sys

list_genenames = []
list_fraction_GC = []

print "hellooo"

while 1:
    print "I'm going into a while loop"
    line = sys.stdin.readline() # stuck here
    print "I just tried to print a line"
    print line
   
    GC_counter = 0.0
    AT_counter = 0.0
    
    if line.startswith(">"):
        print "I'm in a title line"
        gene_id = line
        list_genenames.append(gene_id)
    elif line.startswith("A" or "C" or "T" or "G"):
        print "I'm in a nucleotide line"
        for i in range(len(line)):
            print "help I'm trapped in the nucleotide loop"
            if (line[i] == "G" or line[i] == "C"):
                GC_counter += 1
            elif (line[i] == "A" or line[i] == "T"):
                AT_counter += 1
        fraction_GC = GC_counter / (GC_counter + AT_counter)
        list_fraction_GC.append(fraction_GC)
    elif line == "":
        print "A line is empty"
        break
    print "help I'm trapped in the while loop"

list_tuples = zip(list_genenames, list_sequences)

print list_tuples


#bedtools.getfa