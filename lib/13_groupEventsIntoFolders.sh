#! /bin/bash

cd ../processed_data
mkdir Events

value=$(<uniqueEventsList.txt)

for i in $value ; do
	grep $i EventNCBITaxonTable.txt > Events/$i.txt
done

