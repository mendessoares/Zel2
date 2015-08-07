#!/usr/bin/env python

import sys
import os
import argparse

'''
TODO:
    Include grep part that i needed to run before this script
    Clean up and work on description
    Change name of file
    Create error controls
    Merge with script 4 (which deals with a different file)
    Merge with script 5 (which deals with the files that are output of scripts 3 and 4).
    
    
    
Here I will just write a small file manipulation script to get the species ID from the clean KEGG Genome list of Prokaryotes. 

The lines currently look like this:

  H              eco  Escherichia coli K-12 MG1655
So, they start with a H, then lots of spaces, then the speciesID (which is what I want), then the species and strain name.
In the example above, I want to just fetch 'eco'
the input should be cleancompleteGenomeProkaryotesList.txt
the output should be CompleteSpeciesIDsKEGG.txt
'''

arguments = sys.argv

inputFile = arguments[1]
outputFile = arguments[2]

#fetch the required file
fileName = open(inputFile,'r')
fixedFile = open(outputFile,'w')


#for each line in the file, separate everything by the space, then transfer the info i want (which is in the 15th column),to the new file
for line in fileName:
    new_line = line.split(' ')
    info = new_line[14]
    fixedFile.write(info+'\n')
    
fileName.close()
fixedFile.close()

