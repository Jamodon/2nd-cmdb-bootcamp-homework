#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it.
"""
import sys

from fasta import FASTAReader 
        
reader = FASTAReader( sys.stdin )        

seq_length = []
actual_sequence = []
list_of_duples = []
for sid, sequence in reader:
    seq_length.append(len(str(sequence)))
    actual_sequence.append(str(sequence))
    list_of_duples = zip(seq_length, actual_sequence)
    print list_of_duples
sort_list = sorted(list_of_duples[0], reverse=True)

transcripts = sort_list[0:100]

start_codons = "ATG"
stop_codons = ["TAG", "TGA", "TAA"]

aminoAcidMap = {"TTT" : "F", "TTC" : "F", "TTA" : "L", "TTG" : "L", "TCT" : "S", "TCC" : "S", "TCA" : "S",
                "TCG" : "S", "TAT" : "Y", "TAC" : "Y","TAA" : "stop", "TAG" : "stop", "TGT" : "C", "TGC" : "C",
                "TGA" : "stop", "TGG" : "W", "CTT" : "L","CTC" : "L", "CTA" : "L", "CTG" : "L","CCT" : "P",
                "CCC" : "P", "CCA" : "P", "CCG" : "P","CAT" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q",
                "CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "ATT" : "I", "ATC" : "I","ATA" : "I","ATG" : "M",
                "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "AAT" : "N", "AAC" : "N", "AAA" : "K","AAG" : "K",
                "AGT" : "S", "AGC" : "S", "AGA" : "R","AGG" : "R", "GTT" : "V", "GTC" : "V", "GTA" : "V","GTG" : "V",
                "GCT" : "A","GCC" : "A","GCA" : "A", "GCG" : "A", "GAT" : "D", "GAC" : "D", "GAA" : "E","GAG" : "E",
                "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}

  