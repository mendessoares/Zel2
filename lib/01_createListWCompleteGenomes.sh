#!/bin/bash

#clean the text file that can be downloaded from KEGG with the NCBI taxonomy.

grep ^H ../original_data/completeGenomeProkaryotesList.txt > ../processed_data/completeGenomeListFile.txt