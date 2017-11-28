def prueba():
    mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
    coordenada = seleccionCasillero()
    a = coordenadaCheck(coordenada,mapa)
    while a != "Coordenada Ok":
        print(a)
        coordenada = seleccionCasillero()
        a == coordenadaCheck(coordenada,mapa)
        if a != "Coordenada Ok":
            break
        else:
            continue
    print(coordenada)

def seleccionCasillero():
    """Recibe la coordenada del usuario devuelve una tupla con las coordenadas"""
    coordenada = input("Seleccione casillero: ")
    tuplaCoordenada = (coordenada[0],coordenada[1:])
    return tuplaCoordenada

def coordenadaCheck(coordenada,mapa):
    """Recibe la tupla de coordenadas con el mapa y verifica que la posición existe. Devuelve mensaje si válido o si es error"""
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

    if type(x)!= str or x == "" or x == " ":
        return False
    else:
        x = x.upper()
        if x in mapa[0]:
            return True
        else:
            return False

def filaCheck(y,mapa):
    """Recibe valor de fila seleccionado por el usuario. Devuelve True si valor existe o False en caso contrario"""

    ctdadFilas = len(mapa)
    ctdadFilas = int(ctdadFilas)
    y = int(y)
    valoresFilas = []

    for valor in range (1,ctdadFilas):
        valoresFilas.append(valor)
    if y in valoresFilas:
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



