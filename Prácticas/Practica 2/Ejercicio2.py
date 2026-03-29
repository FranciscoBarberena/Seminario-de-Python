playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

def obtenerMinutosYSegundos(song):
    return song["duration"].split(":")

def obtenerMinutos(minYSeg):
    return int(minYSeg[0])

def obtenerSegundos(minYSeg):
    return int(minYSeg[1])

def obtenerDuracionSegundos(cancion):
    lista = obtenerMinutosYSegundos(cancion)
    return (obtenerMinutos(lista)*60 + obtenerSegundos(lista))

def convertirParaImpresion(duracionSegundos):
    duracionMinutos = duracionSegundos // 60
    duracionSegundos = duracionSegundos % 60
    if (len(str(duracionSegundos))) = 1:
        duracionSegundos =f"0{duracionSegundos}"
    return f"{duracionMinutos}:{duracionSegundos}"
maxSegundos = 0
minSegundos = 999999
duracionTotalSegundos = 0
for song in playlist:
    longitudSegundos = obtenerDuracionSegundos(song)
    if longitudSegundos >maxSegundos:
        maxSegundos = longitudSegundos

        maxCancion = song["title"]
    if longitudSegundos < minSegundos:
        minSegundos = longitudSegundos
        minCancion = song["title"]
    duracionTotalSegundos += obtenerDuracionSegundos(song)


print (f"Duracion total: {convertirParaImpresion(duracionTotalSegundos)}")
print(f"Canción más larga: {maxCancion} {convertirParaImpresion(maxSegundos)}")
print(f"Cancion mas corta: {minCancion} {convertirParaImpresion(minSegundos)}")