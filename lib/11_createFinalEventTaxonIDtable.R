getwd()

setwd("Computation/workspace/Zelezniak_Analysis/MethodsToClean/lib")

#open the blast results
blastTable <- data.frame(read.table("../processed_data/blastResults.txt"))

#open the events table
eventsTable <- data.frame(read.table("../processed_data/otuEventTable.txt"))

#open the table with the match between the KEGG id and the Taxon_Id from NCBI
taxonIdTable <- data.frame(read.table("../original_data/KEGGGenomesWithTaxID.txt",header = T))


#name the columns in the blastTable and the eventsTable
colnames(blastTable) <- c("OTU","Taxon")
colnames(eventsTable) <- c("Event","OTU")

#start by merging the events and blast table by the out identifier
mergedTable <- merge(eventsTable,blastTable, by = "OTU")

#then get the resulting table and merged it with the taxonIdTable by the colum Taxon, with is the KEGG taxonomic ID
mergedTable <- merge(mergedTable, taxonIdTable, by = "Taxon")

#clean up and create a table with only the events id and the NCBI taxonomic ID since this is the ID used in ModelSEED
mergedTable <- mergedTable[,3:4]

#make a list of the unique Events and of the unique Taxa in the dataset
uniqueEvents <- unique(mergedTable$Event)
uniqueTaxa <- unique(mergedTable$Taxonomic_ID)

#Differnet OTUs may have been assigned to the same taxon, os it is possibl ethat one event has repeated taxa reported. Since we only care about the presence/absence of taxa in the event, we want to remove duplicate entries.
uniqueMergedTable <- mergedTable[!duplicated(mergedTable),]


#output everything.
write.table(mergedTable, file = "../processed_data/EventNCBITaxonTable.txt", row.names = F)
write.table(uniqueEvents, file = "../processed_data/uniqueEventsList.txt",row.names = F )
write.table(uniqueTaxa, file = "../processed_data/uniqueTaxaList.txt",row.names = F)
