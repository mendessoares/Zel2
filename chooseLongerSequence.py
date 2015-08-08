#!/usr/bin/env python

from sys import argv


'''
TODO:
    Clean up code
    Insert error dealing
    Try to do everything without needing pandas
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
      To extract only the event and otu id info from the Chaffron dataset
      > getEventAndOTU.py inputFile outputFile
      
SEE ALSO
      other packages that may be useful

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''
