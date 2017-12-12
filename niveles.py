import casillero

mapas = [[["o", "o", ".", "o", "o"],
          ["o", ".", "o", ".", "o"],
          [".", "o", "o", "o", "."],
          ["o", ".", "o", ".", "o"],
          ["o", "o", ".", "o", "o"]],

         [[".", "o", ".", "o", "."],
          ["o", "o", ".", "o", "o"],
          [".", "o", ".", "o", "."],
          ["o", ".", "o", ".", "o"],
          ["o", ".", "o", ".", "o"]],

         [["o", ".", ".", ".", "o"],
          ["o", "o", ".", "o", "o"],
          [".", ".", "o", ".", "."],
          ["o", ".", "o", ".", "."],
          ["o", ".", "o", "o", "."]],

         [["o", "o", ".", "o", "o"],
          [".", ".", ".", ".", "."],
          ["o", "o", ".", "o", "o"],
          [".", ".", ".", ".", "o"],
          ["o", "o", ".", ".", "."]],

         [[".", ".", ".", "o", "o"],
          [".", ".", ".", "o", "o"],
          [".", ".", ".", ".", "."],
          ["o", "o", ".", ".", "."],
          ["o", "o", ".", ".", "."]]]

mapaGanado = [[".", ".", ".", ".", "."],
          [".", ".", ".", ".", "."],
          [".", ".", ".", ".", "."],
          [".", ".", ".", ".", "."],
          [".", ".", ".", ".", "."]]

import random

def cantidadDeNivelesPredeterminado():
    global mapas
    return len(mapas)


"""def mapaNivelPredeterminado(nivel):
    Ingresa entero con número de nivel, devuelve mapa correspondiente a nivel
    global mapas
    return mapas[int(nivel)-1]"""

def mapaNivelPredeterminado(nivel):
    mapas = [[["o", "o", ".", "o", "o"],
              ["o", ".", "o", ".", "o"],
              [".", "o", "o", "o", "."],
              ["o", ".", "o", ".", "o"],
              ["o", "o", ".", "o", "o"]],

             [[".", "o", ".", "o", "."],
              ["o", "o", ".", "o", "o"],
              [".", "o", ".", "o", "."],
              ["o", ".", "o", ".", "o"],
              ["o", ".", "o", ".", "o"]],

             [["o", ".", ".", ".", "o"],
              ["o", "o", ".", "o", "o"],
              [".", ".", "o", ".", "."],
              ["o", ".", "o", ".", "."],
              ["o", ".", "o", "o", "."]],

             [["o", "o", ".", "o", "o"],
              [".", ".", ".", ".", "."],
              ["o", "o", ".", "o", "o"],
              [".", ".", ".", ".", "o"],
              ["o", "o", ".", ".", "."]],

             [[".", ".", ".", "o", "o"],
              [".", ".", ".", "o", "o"],
              [".", ".", ".", ".", "."],
              ["o", "o", ".", ".", "."],
              ["o", "o", ".", ".", "."]]]
    return mapas[int(nivel)-1]

def mapaAleatorio():
    """Genera la cuadrícula para el modo aleatorio.
    Consulta al usuario el tamaño del tablero"""

    tamañoTablero = casillero.tamañoTablero()
    valores = [".","o"]
    mapaNivel = []
    for x in range (0,int(tamañoTablero)):
        fila = []
        for y in range(0,int(tamañoTablero)):
            valor = random.choice(valores)
            fila.append(valor)
        mapaNivel.append(fila)
    return mapaNivel

def mapaAleatorioGanado(tamañoMapa):
    """Recibe tamaño de lista.
    Devuelve mapa ganado, es decir, una lista de listas de mismo tamaño compuesta de puntos"""

    tamañoMapa = int(tamañoMapa)
    mapaGanado = []
    for fila in range(0, tamañoMapa):
        filaMapaGanado = []
        for columna in range(0, tamañoMapa):
            filaMapaGanado.append(".")
        mapaGanado.append(filaMapaGanado)
    return mapaGanado

def puntaje(mapa,movimientos):
    contador = 0
    for fila in mapa:
        for columna in fila:
            if columna == "o":
                contador +=1
    if contador == 0:
        return 500
    elif movimientos == len(mapa)*3:
        return -300
    else:
        return contador * (-50)

