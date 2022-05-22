echo 'filename,filesize' > output.csv # add csv headers

searchDir() {
    filenames=`ls $1`
    for eachfile in $filenames
    do
        if [ -d "$1\/$eachfile" ]; then # is directory? iterate recursively
            searchDir $1\/$eachfile
        else
            filesize=$(du -sb "$1\/$eachfile" | awk '{ print $1 }')
            echo $eachfile,$filesize >> output.csv
        fi
    done
}

firstDir="files"
searchDir $firstDir