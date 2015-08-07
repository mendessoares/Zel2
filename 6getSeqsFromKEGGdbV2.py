#!/usr/bin/env python


import sys
import os
import argparse
import urllib2 as ul

'''TODO
    Clean script
    Change name
    Make output names clearer.

#This script automatically fetches the specific gene sequences that are listed in the clean_matches file from the KEGG api.

#input file should be clean_matches.txt
#output file should be 16SSequences.txt
#errors file should be NotFounds.txt
'''
arguments = sys.argv

inputFile = arguments[1]
outputFile = arguments[2]
errorFile = arguments[3]

clean_matches = open (inputFile,'r')
sequencesFile = open (outputFile,'w')
errors = open (errorFile,'w')

counter = 0

for i in clean_matches:
    i = i.rstrip('\n') #remove new line otherwise it will be included in the search
    try:
    	siteURL = 'http://rest.kegg.jp/get/{:s}/ntseq'.format(i) #put the code into the url line to be fetched
    	print siteURL
    	page = ul.urlopen(siteURL) #get the page from that url. I feel like this and the next (sequence) are steps that slow down everything, and may not be really required.
    	sequence = page.read() #and transfer the information in that page to a new variable
    	print >> sequencesFile, sequence #append the variable sequence to the sequencesFile
    	counter += 1 
    #update the counter . I don't think this is needed. Maybe if I print it from inside the loop I will be able to track how far along the download of the sequences is.
    	print counter
    except ul.URLError,e: #some of the pages gave 404 errors so I changed the program so that it would go back to the beginning of the loop if it encountered on of those errors, instead of crashing.
    	print page,e
    	print >> errors, page
    

clean_matches.close()
sequencesFile.close()
errors.close()
    
    