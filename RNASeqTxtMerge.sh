# Script to merge multiple RNA-Seq Raw Read Counts, FPKM, FPKM-UQ text files into a single matrix
awk 'NF > 1{ a[$1] = a[$1]"\t"$2} END {for( i in a ) print i a[i]}' *.txt > merged.txt
