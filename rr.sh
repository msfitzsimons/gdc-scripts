while IFS='' read -r line || [[ -n "$line" ]]; do
    sam-dump -r $line | head -n 1000 | grep '@RG' > $line'_ReadGroups.txt'
    rm $line.sra.cache 
done < "$1"