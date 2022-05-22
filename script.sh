echo "filename,filesize" > output.csv

fileNames=`ls files/`
for eachfile in $fileNames
do
    filesize=$(du -sb "files/$eachfile" | awk '{ print $1 }')
    echo $eachfile,$filesize >> output.csv
done

