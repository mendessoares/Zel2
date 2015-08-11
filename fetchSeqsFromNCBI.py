#!/usr/bin/env python

from sys import argv
from Bio import Entrez


'''
NAME and SYNOPSIS 
      fetchSeqsFromNCBI.py -- fetch specific amino acid sequences from NCBI Entrez.   
'''

'''
DESCRIPTION
    The script expects a file with the list of sequence ids and a list of taxids form NCBI. It will fetch the sequence of each COG for each species in each list. T
'''

'''
EXAMPLES
      fetch the sequences of the proteins listed in the listOf40COGS.txt file for each of the organisms listed in the third column of the NCBITaxonomyFTP/bacteriaCategories.dmp file
      > python fetchSeqsFromNCBI.py listOf40COGS.txt NCBITaxonomyFTP/bacteriaCategories.dmp 
      
SEE ALSO
      

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

arguments = argv

markersFile = arguments[1]
organismsFile = arguments[2]
allSeqsFile = arguments[3]

Entrez.email = 'soares.maria@mayo.edu'

markers = open(markersFile,'r')
original_organisms = open(organismsFile, 'r')
allSeqs = open(allSeqsFile, 'w')

new_line = []
organisms = []
ids = '' 
record = '' 

for line in original_organisms:
    new_line = line.rstrip()
    new_line = new_line.split('\t')
    if new_line[1] != new_line[2]:
        #print ("they are different")
        code = new_line[2]
        organisms.append(code)
    else:
        continue
    
print organisms

 
for item in markers:
    item = item.rstrip()
    for bug in organisms:
        try:
            handle = Entrez.esearch(db="protein",term="txid%s[Orgn] AND %s[cog]" % (bug, item))
            record = Entrez.read(handle)
            Id = record["IdList"]
            new_handle = Entrez.efetch(db="protein", id= Id, rettype="fasta", retmode="txt")
            seq = new_handle.read()
            if seq.startswith('>'):
                print>>allSeqs, ">", bug, '\t', item, '\t', seq 
            else:
                continue
        except:
            continue
        
allSeqs.close()
markers.close()
original_organisms.close()

exit(0)

