def transformadorCoordenadas(a):
    """Recibe coordenada seleccionada por el jugador y devuelve la ubicación en el mapa"""
    x , y = a
    x = x.lower()
    columnas =["a","b","c","d","e","f","g","h","i","j"]
    x = columnas.index(x)
    return x,int(y)

def mapa(a):
    mapa = ([["o", "o", ".", "o", "o"],
          ["o", ".", "o", ".", "o"],
          [".", "o", "o", "o", "."],
          ["o", ".", "o", ".", "o"],
          ["o", "o", ".", "o", "o"]])
    x,y=transformadorCoordenadas(a)
    return mapa[x][y]

print(mapa("A1"))

