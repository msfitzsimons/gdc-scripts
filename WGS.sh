# Script for downloading WGS BAM files from SRA
while IFS='' read -r line || [[ -n "$line" ]]; do
    prefetch --max-size 200G $line
    sam-dump -r $line.sra | samtools view -bS -> $line.bam
    rm $line.sra.cache
done < "files.txt"

# Get md5sum and file size for downloaded BAM files
md5sum * >> md5s.txt
ls -l >> file_size.txt
awk -F" " '{print $5,'\t',$9}' file_size.txt | grep 'bam' > file_size.tsv
awk -F" " '{print $1,'\t',$2}' md5s.txt | grep 'bam' > md5s.tsv
join -1 2 -2 2 file_size.tsv md5s.tsv > joined_md5_filesize.tsv
rm file_size*
rm md5s*
