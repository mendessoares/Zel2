#!/usr/bin/env python

from sys import argv
import os

'''
TODO:
    Ok, it's already creating a dictionary with the keys. I still need to figure out how to find the longest sequence and add it to its respective key.
'''

'''
NAME and SYNOPSIS 
      findLongestSequenceinaFile.py -- Choose the longest 16S sequence as a representative for each species/strain.   
'''

'''
DESCRIPTION
    The script expects the list of sequences downloaded from the KEGG API. Because each species/strain may have several 16S gene sequences associated with it, the authors
    of the Zelezniak et al paper decided to choose only the longest one as representative [NOTE: I don't think that was a good idea.]. So this script finds the longest one for
    each strain/species and moves it to a new file that will then serve to create a local database of 16S sequences of species with complete genome sequences.
'''

'''
EXAMPLES
      Reduce the data set of representative 16S gene sequences to just one, the longest.
      > python 07_findLongestSequenceinaFile.py
      
SEE ALSO
      Uses output from script 

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

path = '../processed_data/SpeciesSequenceFiles/'

os.chdir(path)
longestSeqs = open('../longestSeqs.fasta','w')

for filename in os.listdir(os.getcwd()):
    group = open(filename,'r')
    longest = '' 
    for item in group:
        if len(item) > len(longest):
            longest = item
    print>>longestSeqs, longest
    
longestSeqs.close()
        
    
    
    
