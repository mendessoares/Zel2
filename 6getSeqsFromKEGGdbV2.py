#!/usr/bin/env python


import sys
import urllib2 as ul


'''TODO
    Clean script
    Change name getSeqsFromKEGGdb.py
    Make output names clearer.
'''

'''
NAME and SYNOPSIS 
      getSeqsFromKEGGdb.py -- Get sequences listed from the KEGG database api
'''

'''
DESCRIPTION
      
      This script expects a file with a list of the species and gene ID for the 16S sequences of only the species/strains with complete genomes. The format of the entries
      should be speciesID:geneID. This script used the output file from script find16SofCompleteGenomes.py .
      
      It accesses the KEGG API and downloads the sequences listed in the input file in the FASTA format.
'''


'''
EXAMPLES
      To get the sequences from the KEGG database
      > getSeqsFromKEGGdb.py cleanMatchesFile sequencesFile errorsFile
      #input file should be Data/cleanMatches.txt
      #output file can be Data/16SSequences.txt
      #errors file can be Data/NotFounds.txt
      
SEE ALSO
      Uses output from find16SofCompleteGenomes.py script.

AUTHORS
      Helena Mendes-Soares - Mayo Clinic, Center for Individualized Medicine 
'''

arguments = sys.argv

cleanMatchesFile = arguments[1]
sequencesFile = arguments[2]
errorsFile = arguments[3]

cleanMatches = open (cleanMatchesFile,'r')
sequences = open (sequencesFile,'w')
errors = open (errorsFile,'w')

counter = 0

for i in cleanMatches:
    i = i.rstrip('\n') #remove new line otherwise it will be included in the search
    try:
    	siteURL = 'http://rest.kegg.jp/get/{:s}/ntseq'.format(i) #put the code into the url line to be fetched
    	print siteURL
    	page = ul.urlopen(siteURL) #get the page from that url.
    	sequence = page.read() #and transfer the information in that page to a new variable
    	print >> sequences, sequence #append the variable sequence to the sequencesFile
    	counter += 1 #update the counter . I don't think this is needed. 
        print counter #just so you know that the program is actually running
    except ul.URLError,e: #some of the pages gave 404 errors so I changed the program so that it would go back to the beginning of the loop if it encountered on of those errors, instead of crashing.
    	print page,e
    	print >> errors, page
    

cleanMatches.close()
sequences.close()
errors.close()
    
    