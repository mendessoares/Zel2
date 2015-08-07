#!/usr/bin/env python

import sys
import os
import pandas as  pd
#import argparse #Not necessary until I know what to do with it.

'''
TODO:
    Remove that intermediate file
    Rename the file
    Clean up code
    Insert error dealing
    Try to do everything without needing pandas
'''




'''
NAME
      TBD -- Extract event and otu IDs from Chaffron (2010) dataset
SYNOPSIS      
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


arguments = sys.argv #store the arguments given by the user in the variable arguments

inputFileName = arguments[1] #The first filename given by the user is the input file
outputFileName = arguments[2] #The second filename given by the used is the final output file


f = open(inputFileName,'r') #open original file

new_table = '' #create empty table <- ACTUALLY, I THINK I'M CREATING AN EMPTY STRING, WHICH MAKES NO SENSE DOING. I SHOULD START WITH [ ]. 

for line in f:
    new_line = line.replace('; otu','\t otu') #put a tab right before the otuID and put this updated line into the newly created table.
    new_table += new_line

f.close()

##let's export the file as a txt because I only know how to import it as a dataframe in pandas from a file. THERE HAS GOT TO BE A WAY TO NOT HAVE TO GO THROUGH THIS PART AND ANALYZE THE TABLE WITH THE TAB BEFORE THE OTUID DIRECTLY

tempFile = open('file.txt','w')

tempFile.write(new_table)
tempFile.close()

f = open('file.txt','r')

##this file has the data with several columns per row. In the first column is the event, and in the 7th column is the otuID/
data = pd.read_table(f,header = None)


events = data[[1]]#ok, this is the info for the event, however, to get the otu info, it is more complicated because apparently the column index doesn't end after the OTU column. Even if the OTU is determined at an earlier taxon, the rest of the columns have Nan
otus = data[[7]]

new_table = pd.concat([otus, events], axis=1)
new_table.columns = ['RepresentativeOTU','Event']
new_table.head()

##now lets just export this to a file containing only the otuID and associated event

otu_Event = open(outputFileName,'w')

new_table.to_csv(otu_Event,sep="\t",index=False)
    
otu_Event.close()

##Now we get the file that is the output of the KEGG annotation. It should have the information of the OTU ID code, and the taxonomic assignment. So, I will break here to learn how to run the KEGG and then come back to this file.

exit(0)