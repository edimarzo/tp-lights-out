def transformadorCoordenadas(a):
    """Recibe coordenada seleccionada por el jugador y devuelve la ubicación en el mapa"""
    x , y = a
    x= x.lower()
    columnas =["a","b","c","d","e","f","g","h","i","j",]
    x = columnas.index(x)
    return x,int(y)

def mapa(a):
    mapa = ([["  |ABCDE"],
             ["1 |oo.oo"],
             ["2 |o.o.o"],
             ["3 |.ooo."],
             ["4 |o.o.o"],
             ["5 |oo.oo"]])
    x,y=transformadorCoordenadas(a)
    for i in range(x,x+1):
        for j in range (y,y+1):
            print(j)
mapa("A1")

