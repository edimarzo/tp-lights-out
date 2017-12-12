import string
import accion
import transformadorCoordenadas

def displayMapa(mapaNivel):
    """Recibe mapa como lista de listas.
    Devuelve el mapa transformado para la visualización del usuario"""

    mapaTransformado = transformadorDeMapa(mapaNivel)
    for linea in mapaTransformado:
        print(linea)

def transformadorDeMapa(mapa):
    """Recibe un mapa como lista de listas.
    Devuelve un mapa con forma de cuadrícula, creado a través de una lista de cadena de caracteres"""

    mapaTransformado = []

    ctdadCaracteresmapa = len(mapa[0])

    primeraLinea= "  |"+string.ascii_uppercase[:ctdadCaracteresmapa]

    mapaTransformado.append(primeraLinea)
    contador = 0
    for linea in mapa:
        contador = contador + 1
        nuevalinea = ""
        for componente in linea:
            nuevalinea = nuevalinea + componente
        nuevalinea = "{} |".format(contador) + nuevalinea
        mapaTransformado.append(nuevalinea)

    return(mapaTransformado)


def transformaMapa(coordenada,mapa):

    #accion.muestraMapa(mapa)

    xInferior,xSuperior,yInferior,ySuperior = transformadorCoordenadas.creeadorDeRangoMapa(coordenada,mapa)

    alto,ancho = transformadorCoordenadas.conversorDeCoordenadas(coordenada)

    mapaVerticalCorregido = accion.prendeApagaVertical(yInferior, ySuperior, alto, mapa)

    mapaHorizontalCorregido = accion.prendeApagaHorizontal(xInferior, xSuperior, ancho, mapaVerticalCorregido)

    mapaFinal = accion.prendeApagaPunto(ancho, alto, mapaHorizontalCorregido)

    #accion.muestraMapa(mapaFinal)

    return mapaFinal



#def prendeApagaMapa(yInferior,ySuperior,columna,xInferior,xSuperior,fila,mapa):

#    mapaVerticalCorregido = accion.prendeApagaVertical(yInferior,ySuperior,columna,mapa)

#    mapaHorizontalCorregido = accion.prendeApagaHorizontal(xInferior,xSuperior,fila,mapaVerticalCorregido)

 #   mapaFinal = accion.prendeApagaPunto(fila, columna, mapaHorizontalCorregido)

#    accion.muestraMapa(mapaFinal)

#    return mapaFinal

#print(transformaMapa("A5",[["o", "o", ".", "o", "o"],["o", ".", "o", ".", "o"],[".", "o", "o", "o", "."],["o", ".", "o", ".", "o"],["o", "o", ".", "o", "o"]]))