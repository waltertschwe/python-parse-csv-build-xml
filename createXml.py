import getopt, sys
from xml.dom.minidom import Document
from dataxml import globalxml, metadataAlbum, trackxml
from csvfile import openFile 

## for arg in sys.argv:
try: 
    file = sys.argv[1] 
    ## print file
except IndexError, e:
    print "pleae pass in a csv file to be processed, arg 1" 
    sys.exit()

rawData = openFile(file)
## rawData = openFile('data.csv')
## print rawData

# Create the minidom document
doc = Document()

# Create the base element
xml = doc.createElement("DATA")
doc.appendChild(xml)

# Create the main root component 
main = doc.createElement("MUSICNET_COMPONENT")
xml.appendChild(main)

## BUILDS THE GLOBAL COMPONENTS
globalxml(doc, main, rawData) 

## BUILD ALBUM LEVEL COMPONENTS
metadataAlbum(doc, main, rawData)

## BUILD TRACK LEVEL COMPONENTS
trackxml(doc, main, rawData)

# print xml
## print doc.toprettyxml(indent="    ")

## FILE = open('file.xml', "w")
## FILE.writelines(doc.toprettyxml(indent="   "))

## WRITE XML TO FILE
for upc in rawData:
    num = upc[0]
    break

## directory = "/root/python/xml/"
directory = "/root/python/xml/data/"
newFile = directory + num + "/" + num + ".xml"
## print newFile
FILE = open(newFile, "w")
FILE.writelines(doc.toprettyxml())
FILE.close()


