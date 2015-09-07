#!/usr/bin/env python

import sys

'''
TODO:
    Create error controls
'''

'''
NAME and SYNOPSIS 
      find16SofCompleteGenomes.py-- From complete list of 16S genes and complete list of species with whole genome sequenced, create a list with the IDs of the 16S genes of 
      only the species that have the whole genome sequenced.
'''

'''
DESCRIPTION
      
      This script expects a file listing the information on the 16S gene sequences that are available in the KEGG database. This list can be found by 
      typing rest.egg.jp/find/genes/16S+RNA in the address field of any (?) web browser. The format is:  speciesid:geneid          description. 
      
      The script also expects a file with the taxonomic information of all the species with complete genome sequences that exist in the KEGG database.This file can be accessed by 
      typing http://www.genome.jp/kegg-bin/get_htext?br08611.keg or go to the KEGG website, then kegg organisms next to KEGG GENOME, then BRITE menu, then Organisms and Cells, then 
      Organisms then  br08611  KEGG prokaryotes in the NCBI taxonomy. You can then just download the htext.
      
      What the script will then do is find the 16S speciesid:geneid for only the species that have the complete genome sequence available.
'''

'''
EXAMPLES
      To get a file containing the 16S gene ID from the KEGG database only for the species that have complete genomes in that database
      >python find16SofCompleteGenomes.py ../processed_data/completeGenomeListFile.txt ../original_data/KEGGList16SandRNA.txt ../processed_data/cleanMatchesFile.txt
      
SEE ALSO
      other packages that may be useful

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''




arguments = sys.argv

completeGenomeListFile = arguments[1]
allInfo16SFile = arguments[2]
cleanMatchesFile = arguments[3]

'''
    FIRST STEP: from complete genomes list to just  the IDs of all the species that have complete genomes in the KEGG database
'''

completeGenomesList = open(completeGenomeListFile,'r')
speciesIDs = []

#for each line in the file, separate everything by the space, then transfer the info I want (which is in the 15th column),to the new file
for line in completeGenomesList:
    if line.startswith('H'):
        new_line = line.split(' ')
        info = new_line[14]
        speciesIDs.append(info+'\n')
    else:
        continue

completeGenomesList.close()    

'''
    SECOND STEP: from the list with all the information of 16S genes in the KEGG database to just the ID code
'''


allInfo16S = open(allInfo16SFile,'r')
justIDs = []

#for each line in the file, separate everything by the space, and tab, and then transfer the information to the new file
for line in allInfo16S:
    new_line = line.split(' ')
    new_line = line.split('\t')
    info = new_line[0]
    justIDs.append(info+'\n')
    
allInfo16S.close()

'''
    THIRD STEP: go through the file with the speciesIDs and the file with the speciesID:geneID codes and create a new file
 with the speciesID:geneID codes for only the species that have the whole genome sequenced.
'''

#first I need to remove \n from the lines in the files
completes = []

for line in speciesIDs:
    new_line = line.rstrip('\n')
    completes.append(new_line)

species_genes = []

for row in justIDs:
    new_row = row.rstrip('\n')
    species_genes.append(new_row)
        

#Now, let's do the matching

matches = []

for i in species_genes:
    for j in completes:
        if j in i:
            matches.append(i)
        else:
            continue
   
#remove duplicate entries
cleanMatches = open (cleanMatchesFile,'w')

clean_matches = list(set(matches))

#sort the list
clean_matches.sort()
    
for m in clean_matches:
    print >> cleanMatches, m
    
cleanMatches.close()

exit(0)

'''
    SUCCESS!!!!
'''
