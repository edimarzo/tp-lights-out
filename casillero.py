def seleccionCasillero(mapa):
    """Recibe mapa transformado en cuadrícula para visualización de usuario y consulta coordenada al usuario.
    Devuelve la coordenada verificada (tanto si existe en la cuadrícula o si los datos ingresados son correctos) como tupla para su posterior utilización."""
    #mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
    coordenada = ingresoCasillero()
    a = coordenadaCheck(coordenada, mapa)
    #print(a)
    while a != True:
        coordenada = ingresoCasillero()
        nuevaCoordenada = coordenadaCheck(coordenada, mapa)
        if nuevaCoordenada == True:
            return coordenada
        else:
            print(nuevaCoordenada)
            continue
    return coordenada

def ingresoCasillero():
    """Recibe la coordenada del usuario devuelve una tupla con las coordenadas"""
    coordenada = input("Seleccione casillero (ingrese vacío para reiniciar el nivel): ")
    if coordenada == "":
        return ""
    else:
        tuplaCoordenada = (coordenada[0],coordenada[1:])
        return tuplaCoordenada


def coordenadaCheck(coordenada,mapa):
    """Recibe la tupla de coordenadas con el mapa y verifica que la posición existe. Devuelve mensaje si válido o si es error"""
    if coordenada == "":
        return True
    else:
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
            return True


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
    #y = int(y)
    valoresFilas = []

    for valor in range (1,ctdadFilas):
        valoresFilas.append(str(valor))
    if y in valoresFilas:
        return True
    else:
        return False


#seleccionCasillero(['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo'])

