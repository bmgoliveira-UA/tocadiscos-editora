
## MAKING DIFFERENT TABLES ##
authorsColumn = ['','','','','','',]
albumsColumn = []


tracksUsableFile = open('data/raw_tracks.csv', 'r', encoding='utf-8-sig' )
tracksUsableData = tracksUsableFile.readlines()
tracksUsableFile.close()

campos = tracksUsableData[0].replace('\n', '').split(',')

print(campos)


## creating authors table

authorsTable = open('data/authors_table.csv', 'w', encoding='utf-8-sig')

authorsTable.close()


## creating albums table

albumsTable = open('data/albums_table.csv', 'w', encoding='utf-8-sig')

albumsTable.close()


## ----FIM---- MAKING DIFFERENT TABLES ##