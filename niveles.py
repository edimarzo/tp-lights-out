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


def cantidadDeNivelesPredeterminado():
    global mapas
    return len(mapas)


def mapaNivelPredeterminado(nivel):
    """Ingresa entero con número de nivel, devuelve mapa correspondiente a nivel"""
    global mapas
    return mapas[int(nivel)-1]
