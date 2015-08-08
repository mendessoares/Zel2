#!/usr/bin/env python

import sys

'''
TODO:
    Clean up and work on description
    Change name of file
    Create error controls
'''

'''
NAME and SYNOPSIS 
      getEventAndOTU.py -- Extract event and otu IDs from Chaffron (2010) dataset   
'''

'''
DESCRIPTION
      
      This script expects a gg_sample_details_otus_filtered_file.d.**.tsv file with information from Chaffron et al (2010) A global network of coexisting microbes from
        environmental and whole-genome sequence data, Genome Research, 20:947-959. Each line has the following information: line number; event number; authors of the paper; 
        title of the paper; taxonomic information of the associated otu.
        The otuID is listed in the end of the line with the taxonomic assignment. Each event may then have several otu's associated with it. Additionally, each environment 
        can have several events associated with it because it is possible that each environment was sampled by different authors.

        To replicate the analysis from the Zelezniak paper, the information we need from this file is the EventIDs and their associated OtuIDs.
        
        The program will get the input file, separate the OtuID from the taxonomic assignment, create an intermediate file where the otuID is in a separate column from the 
        taxonomic ID, then get the table on that file, and extract only the meaningful columns, which will be 1 and 7.
        
        Per information from the Zelezniak_2015 paper, I figured out that the data that was used was the one in the file gg_sample_details_otus_filtered_file.d.03.tsv. 
        The final output file will be otuEventTable.txt
'''

'''
EXAMPLES
      To get a file containing the 16S gene ID from the KEGG database only for the species that have complete genomes in that database
      > getEventAndOTU.py completeGenomeListFile allInfo16SFile cleanMatchesFile(output)
      
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
