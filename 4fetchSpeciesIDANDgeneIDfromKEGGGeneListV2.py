#!/usr/bin/env python

import sys
import os
import pandas as pd
import argparse

'''
#Here I will just write a small file manipulation script to get the species ID from the clean KEGG Genome list of Prokaryotes.
#
#The lines currently look like this:
# ptr:16S_rRNA	16S ribosomal RNA; K01982 large subunit ribosomal RNA
#I really just want to fetch the prt:16S_rRNA part. So I need to separate and then just get the element in index 0. This script is very similar to the script 3fetchSpeciesIDfromKEGGGenomeListV2.py

#input file should be KEGGList16SandRNA.txt
#output file should be SpeciesGeneIDs.txt
'''

arguments = sys.argv

inputFile = arguments[1]
outputFile = arguments[2]

fileName = open(inputFile,'r')
fixedFile = open(outputFile,'w')


#for each line in the file, separate everything by the space, and tab, and then transfer the information to the new file
for line in fileName:
    new_line = line.split(' ')
    new_line = line.split('\t')
    info = new_line[0]
    fixedFile.write(info+'\n')
    
fileName.close()
fixedFile.close()
