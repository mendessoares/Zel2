#!/usr/bin/env python

from sys import argv
from csv import writer



'''
TODO:
  
'''

'''
NAME and SYNOPSIS 
      05_listOrganismIDs.py 
'''

'''
DESCRIPTION
    
'''

'''
EXAMPLES
      > python 05_listOrgIDScreateSeqTable.py ../processed_data/trimmed16SSequences.txt 
      
SEE ALSO
      Uses output from script removeEndLineinFASTAFiles.py

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

arguments = argv

trimmedSequencesFile = arguments[1]


trimmedSequences = open(trimmedSequencesFile, 'r')
sequenceTable = open("../processed_data/sequenceTable.txt",'w')



fixedSequences = []
codes = []

for line in trimmedSequences:
    if line.startswith('>'):
        line = line.split(":")
        codes.append(line[0])
        fixedSequences.append(line[0])
    else:
        fixedSequences.append(line)

codes = list(set(codes))    

print codes


sequences = []
id = []



for linha in range(0,len(fixedSequences)):
    for i in codes:
        if i in fixedSequences[linha]:
            sequences.append(fixedSequences[linha+1])
            id.append(fixedSequences[linha])
            print>>sequenceTable, fixedSequences[linha],'\t', fixedSequences[linha+1]
            
            
        

trimmedSequences.close()
sequenceTable.close()


exit(0)


'''
SUCCESS!!!
'''
