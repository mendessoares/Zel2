#!/usr/bin/env python

from sys import argv

'''
TODO:
    Actually write the script
    Insert error dealing
'''

'''
NAME and SYNOPSIS 
      chooseLongerSequence.py -- Choose the longest 16S sequence as a representative for each species/strain.   
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
      > python chooseLongerSequence.py Data/16SSequences.txt Data/longest16SSequences.txt
      
SEE ALSO
      Uses output from script getSeqsFromKEGGdb.py

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

arguments = sys.argv

allSequencesFile = arguments[1]
longestSequencesFile = arguments[2]

'''
I'm thinking a dictionary for each species ID. Because then you would have a unique sequence for each strain.

Pseucode (kind of... sort of...):

newDictionary = dict()

for line in allSequences:
    if line.startswith(>):
        line.split(:)
        newDictionaryKey = line[1]
    
    else:
        if len(line) > newDictionary[key]:
            newDictionary[key] = line
    
    print >> longestSequence, key, newDictionary[key]
            
'''
