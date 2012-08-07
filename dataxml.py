##########################################
##   Name: readFile
##   params: file    -filename to be read 
##   return: file 
##########################################
def globalxml(doc, main, rawData):

    ## upc = []
    for items in rawData:
        ## upc.append(items[0])
        upc = items[0]
        labelCode = items[4]
        corpCode = items[5]
        artistName = items[6]

     
    code = doc.createElement("MUSICNET_COMPONENT_CODE")
    main.appendChild(code)
    upcData = doc.createTextNode(upc)
    code.appendChild(upcData)

    component = doc.createElement("COMPONENT_TYPE")
    componentData = doc.createTextNode("ALBUM")
    main.appendChild(component)
    component.appendChild(componentData)

    corp_code = doc.createElement("CORP_CODE")
    corpData = doc.createTextNode(corpCode)
    main.appendChild(corp_code)
    corp_code.appendChild(corpData)

    label_code = doc.createElement("LABEL_CODE")
    labelData = doc.createTextNode(labelCode)
    main.appendChild(label_code)
    label_code.appendChild(labelData)

    artist = doc.createElement("ARTIST")
    main.appendChild(artist)
    type = doc.createElement("TYPE")
    value = doc.createElement("VALUE")
    typeData = doc.createTextNode("ARTIST")
    valueData = doc.createTextNode(artistName)
    artist.appendChild(type) 
    artist.appendChild(value)
    type.appendChild(typeData)
    value.appendChild(valueData)
    

    return

def metadataAlbum(doc, main, rawData):
    for items in rawData:
        upc = items[0]
        tracks = items[3]
        album = items[7]
        releaseDate = items[12]
        genre = items[13]
        parentAdvisory = items[14]
        duration = items[16]
        digitalavail = items[17]
        break
         
    ## artist = doc.createElement("ARTIST")

    ## main.appendChild(artist)
    ## artist.appendChild(doc.createElement("TYPE"))
    ## artist.appendChild(doc.createElement("VALUE"))

    vals = ["TRACKS","TITLE","GENRE","RELEASE_DATE","PARENTAL_ADVISORY",
            "RELATED_UPC","DURATION"]

    for x in vals:
        meta = main.appendChild(doc.createElement("METADATA"))
        type = meta.appendChild(doc.createElement("TYPE"))
        value = meta.appendChild(doc.createElement("VALUE"))
        typeData = doc.createTextNode(x)
        if x == "TRACKS":
            tracksData = doc.createTextNode(tracks)
            value.appendChild(tracksData)
        if x == "TITLE":
            titleData = doc.createTextNode(album)
            value.appendChild(titleData)
        if x == "GENRE":
            genreData = doc.createTextNode(genre)
            value.appendChild(genreData)
        if x == "RELATED_UPC":
            upcData = doc.createTextNode(upc)
            value.appendChild(upcData)
        if x == "PARENTAL_ADVISORY":
            parentData = doc.createTextNode(parentAdvisory)
            value.appendChild(parentData)
        if x == "RELEASE_DATE":
            releaseData = doc.createTextNode(releaseDate)
            value.appendChild(releaseData)
        if x == "DURATION":
            durationData = doc.createTextNode(duration)
            value.appendChild(durationData)

        type.appendChild(typeData)
 
    if digitalavail == "WW-MN":
        print "digital avail == 1"
    else:
        print "digital avail != 1"
        
        
    return

def trackxml(doc, main, rawData):
    ## print "TRACK LEVEL: work to do here" 
    vals = ["TITLE","GENRE","DISC_NUMBER","TRACK_NUMBER","ISRC","DURATION","PARENTAL_ADVISORY","RELEASE_DATE","RELATED_UPC","ARTIST"]

    for item in rawData:
        upc = item[0]
        track = item[2]

        component = doc.createElement("MUSICNET_COMPONENT")
        main.appendChild(component)
        
        code  = doc.createElement("MUSICNET_COMPONENT_CODE")
        component.appendChild(code)
        codeData = doc.createTextNode(upc)
        code.appendChild(codeData)

        componentType = doc.createElement("COMPONENT_TYPE")
        component.appendChild(componentType)
        componentData = doc.createTextNode("TRACK") 
        componentType.appendChild(componentData) 
        
        corp_code = doc.createElement("CORP_CODE")
        component.appendChild(corp_code)

        label_code = doc.createElement("LABEL_CODE")
        component.appendChild(label_code)

        for x in vals:
            metadata = doc.createElement("METADATA")
            type = doc.createElement("TYPE")
            value = doc.createElement("VALUE")

            component.appendChild(metadata)
            metadata.appendChild(type)
            metadata.appendChild(value)  

            typeData = doc.createTextNode(x)
            if x == "TRACK_NUMBER":
                trackData = doc.createTextNode(track)
                value.appendChild(trackData)
            type.appendChild(typeData)

    return

