while IFS='' read -r line || [[ -n "$line" ]]; do
     gdc-client upload $line -t token.txt
done < "UUIDS.txt"
