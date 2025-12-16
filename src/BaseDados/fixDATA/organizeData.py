from csv import DictReader
from dataFormat import feedAlbums, updateAlbums, feedAuthors, updateAuthors

## MAKING DIFFERENT TABLES ##
authorsData = []
albumsData = []

authorsDict = {}
albumsDict = {}

tracksUsableFile = open('data/raw_tracks.csv', 'r', encoding='utf-8-sig' )
tracksUsableData = list(DictReader(tracksUsableFile.readlines())) # transforma cada line numa lista
tracksUsableFile.close()


## organize data into authors and albums tables

for line in tracksUsableData[1:]:

    # descartar entradas desnecessárias
    try:
        artist_id = int(line['artist_id'])
        album_id = int(line['album_id'])
    except:
        continue


    # Inicializar o dicionário
    if len(authorsDict) == 0 and len(albumsDict) == 0:
        feedAuthors(authorsDict, line)
        feedAlbums(albumsDict, line) 

    # Adicionar novas entradas OU atualizar entradas existentes
    if len(authorsDict) > 0 and len(albumsDict) > 0:

        # Authors
        # Adicionar novo Autor
        if  artist_id not in authorsDict:
            try:
                feedAuthors(authorsDict, line)
            except:
                continue

        # Adicionar dados a autor já existente
        elif artist_id in authorsDict:
            try:
                updateAuthors(authorsDict, line)
            except:
                continue


        # Albums
        # Adicionar novo album
        if album_id not in albumsDict:
            try:
                feedAlbums(albumsDict, line)
            except:
                continue


        # Adicionar dados a a album já existente
        elif album_id in albumsDict:
            try:
                updateAlbums(albumsDict, line)
                print(albumsDict(album_id)['tracks'])
            except:
                continue

for item in albumsDict:
    if len(albumsDict[item]['tracks']) > 1:
        print(albumsDict[item]['tracks'])

## creating authors table

# authorsTable = open('data/authors_table.csv', 'w', encoding='utf-8-sig')
# authorsTable.writelines()
# authorsTable.close()


## creating albums table

# albumsTable = open('data/albums_table.csv', 'w', encoding='utf-8-sig')
# albumsTable.writelines()
# albumsTable.close()


## ----FIM---- MAKING DIFFERENT TABLES ##