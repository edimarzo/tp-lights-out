import string
def transformadorDeMapa(mapa):
    """Recibe un mapa como lista de listas y devuelve un mapa con forma de cuadrícula, creado a través de una lista de cadena de caracteres"""

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




print(transformadorDeMapa([['.', 'o', '.', 'o', '.'], ['o', 'o', '.', 'o', 'o'], ['.', 'o', '.', 'o', '.'], ['o', '.', 'o', '.', 'o'], ['o', '.', 'o', '.', 'o']]))