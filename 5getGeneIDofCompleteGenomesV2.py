#!/usr/bin/env python

import sys
import os
import pandas as pd
import argparse

'''#Script to go through the file with the speciesIDs of the species that have complete sequenced genomes and the file with the speciesID:geneID codes and create a new file with the speciesID:geneID codes for only the species that have the whole genome sequenced.

#input files should be CompleteSpeciesIDsKEGG.txt (first argument) and SpeciesGeneIDs.txt (second argument)
#output file should be clean_matches.txt (third argument)
'''


arguments = sys.argv

inputFileCompleteSpecies = arguments[1]
inputFileSpeciesGenes = arguments[2]
outputFile = arguments[3]

#get the files with the speciesIDs of the species that have complete genome sequencing and the available speciesID:geneID
file_completes = open(inputFileCompleteSpecies,'r')
file_species_genes = open(inputFileSpeciesGenes,'r')

#first I need to remove \n from the lines in the files
completes = []

for line in file_completes:
    new_line = line.rstrip('\n')
    completes.append(new_line)

species_genes = []

for row in file_species_genes:
    new_row = row.rstrip('\n')
    species_genes.append(new_row)
        

#Now, let's do the matching

clean_matchesFile = open (outputFile,'w')

matches = []

for i in species_genes:
    for j in completes:
        if j in i:
            matches.append(i)
        else:
            continue


#for some reason it is creating a whole bunch of duplicate entries...  PROBLEM TO FIX!         
#remove duplicate entries
clean_matches = list(set(matches))


#sort the list
clean_matches.sort()
    
for m in clean_matches:
    print >> clean_matchesFile, m
    
    
#matchesFile.close()
clean_matchesFile.close()

#SUCCESS!!!!
