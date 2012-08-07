clear
echo "Hi, $USER!"
echo "Startup.. Python about to process files"

FILES="*"
  ##  python ../createXml.py $file 
for file in csv/*.csv;
do 
    echo "Processing $file file.........."; 
    python createXml.py $file 

done

echo "Finished, $USER!"
echo "XML Creation Completed!"
