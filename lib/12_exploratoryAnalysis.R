#looking at the merged data.

setwd("Computation/workspace/Zelezniak_Analysis/MethodsToClean/lib")

eventTaxon <- read.table("../processed_data/EventNCBITaxonTable.txt",header=T)

unique(eventTaxon$Event)

numberTaxaPerEvents <- data.frame(table(eventTaxon$Event))


numberEvent2OrMoreTaxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq>1,]

numberEvent3OrMoreTaxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq>3,]

numberEvent4OrMoreTaxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq>4,]

numberEvent5OrMoreTaxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq>5,]

numberEvent1Taxon <- numberTaxaPerEvents[numberTaxaPerEvents$Freq==1,]

numberEvent2Taxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq==2,]

numberEvent3Taxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq==3,]

numberEvent4Taxa <- numberTaxaPerEvents[numberTaxaPerEvents$Freq==4,]

#plot some graphs
plot(numberTaxaPerEvents, main = "Number of taxa in each event", axes= F, xlab = "Events", ylab = "Number of taxa")
abline(h=0)
axis(side = 2, at = c(0,50,100,150,200,250,300))

plot(numberEvent5OrMoreTaxa, main = "Number of taxa in each event for events with 5 or more taxa", axes= F, xlab = "Events", ylab = "Number of taxa")
abline(h=0)
axis(side = 2, at = c(0,50,100,150,200,250,300))
