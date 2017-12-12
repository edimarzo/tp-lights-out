import accion

def conversorDeCoordenadas(coordenada):
    """Recibe tupla de coordenadas seleccionada por el jugador.
    Devuelve la ubicación correspondiente al mapa de la lista de listas"""

    x , y = coordenada
    x = x.lower()
    columnas =["a","b","c","d","e","f","g","h","i","j"]
    x = columnas.index(x)
    y = int(y)-1
    return (int(x),int(y))

#def mapa(a):
#    mapa = ([["o", "o", ".", "o", "o"],
#          ["o", ".", "o", ".", "o"],
#          [".", "o", "o", "o", "."],
#          ["o", ".", "o", ".", "o"],
#          ["o", "o", ".", "o", "o"]])
#    x,y=transformadorCoordenadas(a)
#    return mapa[x][y]


def creeadorDeRangoMapa(coordenada, mapa):
    """Recibe tupla de coordenadas y el mapa como lista de listas.
    Devuelve el rango horizontal y vertical"""

    x,y = conversorDeCoordenadas(coordenada)
    rangoXInf,rangoXSup = creadorRangoPunto(x,mapa)
    rangoYinf,rangoYSup = creadorRangoPunto(y,mapa)
    return (rangoXInf,rangoXSup,rangoYinf,rangoYSup)

def creadorRangoPunto(valor,mapa):
    """Recibe un valor y el mapa como lista de listas.
    Calcula el rango inferior y superior en función del mapa."""

    rangoInferior = valor - 1
    rangoSuperior = valor + 2
    if rangoInferior <= 0:
        rangoInferior = 0
    elif rangoSuperior >= len(mapa):
        rangoSuperior = len(mapa)
    return (rangoInferior,rangoSuperior)

#def recorreMapa(coordenada,mapa):
#    xInferior,xSuperior,yInferior,ySuperior = creeadorDeRangoMapa(coordenada,mapa)
#    alto,ancho = conversorDeCoordenadas(coordenada)

#    accion.muestraMapa(mapa)

#    for x in range (yInferior,ySuperior):
#        for y in range (alto,alto+1):
#            mapa[x][y] = accion.prendeApaga(mapa[x][y])

#    for w in range (ancho):
#        for z in range(xInferior,xSuperior):
#            mapa[w][z] = accion.prendeApaga(mapa[w][z])

#    accion.muestraMapa(mapa)

#print(recorreMapa("A1",[["o", "o", ".", "o", "o"],["o", ".", "o", ".", "o"],[".", "o", "o", "o", "."],["o", ".", "o", ".", "o"],["o", "o", ".", "o", "o"]]))
