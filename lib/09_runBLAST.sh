#!/bin/bash

cd /usr/local/ncbi/blast/bin

blastn -query ~/Computation/workspace/Zelezniak_analysis/MethodsSept2015/original_data/otus_rep_seqs_gi.d.03.txt -db ~/Computation/workspace/Zelezniak_analysis/MethodsSept2015/db/16Sdatabase -outfmt 10 -max_target_seqs 1 -out ~/Computation/workspace/Zelezniak_analysis/MethodsSept2015/processed_data/blastResults.csv

cd ~Computation/workspace/Zelezniak_Analysis/MethodsSept2015/lib