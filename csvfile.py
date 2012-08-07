##########################################
##   Name: readFile
##   params: file    -filename to be read 
##   return: file 
##########################################
import os
import csv

def openFile(file):
    data = csv.reader(open(file, "rb"))
    data_list = []
    data_list.extend(data)
    upc = []

    for items in data_list:
        upc.append(items[0])

    createDir(upc) 

    return data_list

def createDir(upc):
    dir = "/root/python/xml/data/" 
    for item in upc: 
        try:
            os.makedirs(dir + item)
            directory = "/root/python/xml/data/"
            newFile = directory + item + "/" + item + ".xml"
            FILE = open(newFile, "w")
            FILE.close()
        except OSError:
            if os.path.exists(dir + item):
                pass
            else:
                raise
    return
