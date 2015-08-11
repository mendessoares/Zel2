#!/usr/bin/env python

from sys import argv
from csv import writer
from Finder.Finder_items import item

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
      > python chooseLongerSequence.py Data/16SSequences.txt Data/longest16SSequences.txt
      
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
newKey = ''
newValue = None

for line in trimmedSequences:
    if line.startswith('>'):
        line = line.split(":" )
        #print>>longestSequences, line[0]
        if line[0] not in newDictionary.keys():
            newKey = line[0]
            newDictionary.update({newKey:newValue})
            
        else:
            continue
        
    #else:
        #if len(line) > len(newDictionary[newKey]):
            #newDictionary[newKey] = line
    
    

'''
MAYBE... I can start the dictionary to create the keys, then go over each line that has those keys in the above line and find the longest sequence.
'''
        
longest = None
'''
for line in trimmedSequences:
    for key in newDictionary:
        if line == key:
            sequence = line[i+1]
            if len(sequence)>len(longest)
            longest = sequence
            newDictionary[key] = longest
            



'''

writerDict = writer(longestSequences)

for key, value in newDictionary.items():
    writerDict.writerow([key,value])
    

trimmedSequences.close()
longestSequences.close() 


'''
I'm thinking a dictionary for each species ID. Because then you would forcibly have a unique sequence for each strain.

Pseucode (kind of... sort of...):

newDictionary = dict()

for item in sequences:
    if line.startswith(>):
        line.split(:)
        if line[0] not in D:
            newDictionary[line[0]] = None
        else:
            continue
            
            
    else:
        if len(line) > newDictionary[key]:
            newDictionary[key] = line
    
    print >> longestSequence, key, newDictionary[key]
    
    
Somewhere in this script I also want to translate the speciesID code to the actual species/strain name which means I probably need to go into the KEGG db again. Actually no, I just 
need to go to the file with the completeGenomeProkaryotesList.txt in the Data folder
            
'''
