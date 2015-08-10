#!/usr/bin/env python

from sys import argv

'''
NAME and SYNOPSIS 
      removeEndLineinFASTAFiles.py -- remove the end of the line in the sequence part of FASTA files.   
'''

'''
DESCRIPTION
    The script expects a FASTA file where the sequence part (the lines that don't have >) is divided by /n . This script removes the /n. May be used for any FASTA file
    downloaded from the "interwebs"
'''

'''
EXAMPLES
      Remove the /n part from the seqeunce part of FASTA files.
      > python removeEndLineinFASTAFiles.py Data/16SSequences.txt Data/trimmed16SSequences.txt
      
SEE ALSO
      Uses output from script getSeqsFromKEGGdb.py (for instance)

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

arguments = argv

allSequencesFile = arguments [1]
trimmedSequencesFile = arguments[2]


allSequences = open(allSequencesFile, 'r')
trimmedSequences = open(trimmedSequencesFile, 'w')


#sequences = []
seq = ''
    
for line in allSequences:
    if line.startswith('>'):
        seq += '\n'
        seq += line
    else:
        seq += line.rstrip()

                
print>>trimmedSequences, seq
    
    
allSequences.close()
trimmedSequences.close()

exit(0)

#SUCCESS!!!