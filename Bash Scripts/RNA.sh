# Script for downloading RNA-Seq files from SRA
while IFS='' read -r line || [[ -n "$line" ]]; do
    prefetch --max-size 200G $line
    fastq-dump -I --split-files $line.sra
    tar -zcvf ${line}_1.tgz ${line}_1.fastq
    tar -zcvf ${line}_2.tgz ${line}_2.fastq
	rm $line.sra.cache
    rm $line.sra
    rm ${line}_1.fastq
    rm ${line}_2.fastq
done < "files.txt"

# Get md5sum and file size for downloaded BAM files
md5sum * >> md5s.txt
ls -l >> file_size.txt
awk -F" " '{print $5,'\t',$9}' file_size.txt | grep 'tgz' > file_size.tsv
awk -F" " '{print $1,'\t',$2}' md5s.txt | grep 'tgz' > md5s.tsv
join -1 2 -2 2 file_size.tsv md5s.tsv > joined_md5_filesize.tsv
rm file_size*
rm md5s*
