def prueba():
    mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
    coordenada = seleccionCasillero()
    a = coordenadaCheck(coordenada,mapa)
    print(a)


def seleccionCasillero():
    coordenada = input("Seleccione casillero")
    tuplaCoordenada = (coordenada[0],coordenada[1:])
    return tuplaCoordenada

def coordenadaCheck(coordenada,mapa):
    x,y = coordenada
    resultadox = columnaCheck(x,mapa)
    resultadoy = filaCheck(y,mapa)

    if resultadox == False and resultadoy == False:
        return "Ingrese correctamente las coordenadas de columna y fila"
    elif resultadox == True and resultadoy == False:
        return "Ingrese correctamente el valor de la fila"
    elif resultadox == False and resultadoy == True:
        return "Ingrese correctamente el valor de la columna"
    else:
        return "Coordenada Ok"


def columnaCheck(x,mapa):
    """ Ingresa mapa y valor de columna seleccionado por el usuario. Devuelve el valor verificado o error."""

    x = x.upper()
    if x in mapa[0]:
        return True
    else:
        return False

def filaCheck(y,mapa):

    ctdadFilas = len (mapa)
    filasMapa = []

    if int(y) > ctdadFilas:
        return False

    else:
        for x in range (1,ctdadFilas):
            filasMapa.append(mapa[x][0])

        if y in filasMapa:
            return True
        else:
            return False


prueba()

"""def transformadorCoordenadas(a):
    x , y = a
    x = x.lower()
    columnas =["a","b","c","d","e","f","g","h","i","j"]
    x = columnas.index(x)
    return x,int(y)"""



