"""Recibe mapa como lista de listas y coordenada seleccionada por usuario como tupla, acciona sobre el mapa"""

"""mapa = [[".", ".", ".", "o", "o"],
          [".", ".", ".", "o", "o"],
          [".", ".", ".", ".", "."],
          ["o", "o", ".", ".", "."],
          ["o", "o", ".", ".", "."]]"""

def prendeApaga(a):
    """Recibe caracter de mapa como lista de lista.
    Devuelve el punto en función de su """
    if a == ".":
        return "o"
    elif a == "o":
        return "."

def muestraMapa(mapa):
    """ Recibe mapa como lista de lista.
    Muestra el mapa al usuario."""

    for linea in mapa:
        print(linea)
    print(" ")

def prendeApagaVertical (yInferior,ySuperior,alto,mapa):
    "Recibe el rango dentro del cual se debe recorrer el mapa verticalmente junto con el mapa y la columna seleccionada por el usuario."
    "Devuelve el mapa luego de aplicar la función prendeApaga en sentido vertical."

    for x in range(yInferior, ySuperior):
        for y in range(alto, alto + 1):
            mapa[x][y] = prendeApaga(mapa[x][y])
    return mapa

def prendeApagaHorizontal (xInferior,xSuperior,ancho,mapa):
    "Recibe el rango dentro del cual se debe recorrer el mapa horizontalmente junto con el mapa y la fila seleccionada por el usuario."
    "Devuelve el mapa luego de aplicar la función prendeApaga en sentido horizontal."

    for w in range(ancho,ancho+1):
        for z in range(xInferior, xSuperior):
            mapa[w][z] = prendeApaga(mapa[w][z])
    return mapa

def prendeApagaPunto(alto,ancho,mapa):
    "Recibe el punto seleccionado por el usuario junto con el mapa."
    "Devuelve el mapa luego de aplicar la función prendeApaga en el punto."

    mapa[alto][ancho] = prendeApaga(mapa[alto][ancho])
    return mapa





