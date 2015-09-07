README for Zelezniak analysis

You should be able to get the data to the point were you have the list of events with the corresponding taxa identified.

So, here are the steps:

01. 01_createListWCompleteGenomes.sh
02. 02_find16SofCompleteGenomes.py
03. 03_getSeqsFromKEGGdb.py
04. 04_removeEndLineinFASTAfiles.py
05. 05_listOrganismIDs.py
06. Open a new notepad file called codes.txt
07. Copy the output on the terminal from 05_listOrganismIDs.py
08. Paste it to codes.txt
09. On codes.txt replace ,space by \n, then replace ' for nothing, \[ for nothing and \] for nothing.
10. 06_distributeSeqstoSpeciesFiles.sh
11. 07_findLongestSequenceinaFile.py
12. Replace \t by \n in longestSeqs.fasta
13. 08_createLocal16Sdb.sh
14. 09_runBLAST.sh
15. Open blastResults.csv in text editor
16. Replace , and | for \t.
17. Save as blastResults.txt
18. Open in LibreOffice or Excel and remove column 1 and 4 onwards
19. 10_getEventandOTU.py
20. 11_createFinalEventTaxonIDTable.R
21. 12_exploratoryAnalysis.R
22. 13_groupEventsIntoFolders.sh