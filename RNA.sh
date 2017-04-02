while IFS='' read -r line || [[ -n "$line" ]]; do
    fastq-dump -X 1 -Z $line | head -n 1
    rm $line.sra.cache 
done < "$1"