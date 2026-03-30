
def execute3():
    review = """La película sigue a un grupo de astronautas que
    viajan a Marte
    en una misión de rescate. El capitán Torres lidera al equipo
    a través
    de tormentas solares y fallos en el sistema de navegación. Al
    llegar
    a Marte descubren que la base está abandonada y los
    suministros
    destruidos. Torres decide sacrificar la nave nodriza para
    salvar
    al equipo y logran volver a la Tierra en una cápsula de
    emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje
    secreto."""

    listaPalabrasSpoiler= (input("Ingrese las palabras spoiler (separadas por coma): ")).lower().split(",")
    listaPalabrasSpoiler = [spoiler.strip() for spoiler in listaPalabrasSpoiler]
    listaCompletaDePalabras = review.split()
    reviewSinSpoilers=""
    for palabra in listaCompletaDePalabras:
        if palabra.lower() in listaPalabrasSpoiler:
            reviewSinSpoilers += f"{len(palabra)*"*"} "
        else:
            reviewSinSpoilers+= f"{palabra} "
    print(reviewSinSpoilers)