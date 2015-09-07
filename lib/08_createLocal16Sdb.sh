#!/bin/bash

cd /usr/local/ncbi/blast/bin

makeblastdb -in ~/Computation/workspace/Zelezniak_Analysis/MethodsSept2015/processed_data/longestSeqs.fasta -out ~/Computation/workspace/Zelezniak_Analysis/MethodsSept2015/db/16Sdatabase -dbtype nucl

cd ~Computation/workspace/Zelezniak_Analysis/MethodsSept2015/lib