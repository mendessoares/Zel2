#!/usr/bin/env python

from sys import argv
from csv import writer


'''
TODO:
    Ok, it's already creating a dictionary with the keys. I still need to figure out how to find the longest sequence and add it to its respective key.
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
      > python chooseLongerSequence.py Data/trimmed16Ssequences.txt Data/longest16Ssequences.txt
      
SEE ALSO
      Uses output from script removeEndLineinFASTAFiles.py

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

arguments = argv

trimmedSequencesFile = arguments[1]
longestSequencesFile = arguments[2]

trimmedSequences = open(trimmedSequencesFile, 'r')
longestSequences = open(longestSequencesFile, 'w')


newDictionary = dict()



fixedSequences = []
codes = []

for line in trimmedSequences:
    if line.startswith('>'):
        line = line.split(":")
        fixedSequences.append(line[0])
        codes.append(line[0])
    else:
        fixedSequences.append(line)

codes = list(set(codes))    

print codes
longest = []


for linha in range(0,len(fixedSequences)):
    for i in codes:
        if i in fixedSequences[linha]:
            sequence = fixedSequences[linha+1]
        
            if len(sequence) > len(longest):
                longest = sequence
                longest = longest.strip()
            
            newDictionary.update({i:longest})
            
print newDictionary            
        



        
writerDict = writer(longestSequences,delimiter='\n')

for key, value in newDictionary.items():
    writerDict.writerow([key,value])

trimmedSequences.close()
longestSequences.close() 

exit(0)


'''
SUCCESS!!!
'''
