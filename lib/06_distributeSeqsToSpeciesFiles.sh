#!/bin/bash


cd ../processed_data
value=$(<codes.txt)

mkdir SpeciesSequenceFiles

for i in $value ; do
	grep \>$i sequenceTable.txt > SpeciesSequenceFiles/$i.txt
done

