def mapaNivelPredeterminado(nivel):
    """ Ingresa entero con número de nivel, devuelve mapa correspondiente a nivel."""

    if nivel == 1:
        mapa = ([["  |ABCDE"],
                ["1 |oo.oo"],
                ["2 |o.o.o"],
                ["3 |.ooo."],
                ["4 |o.o.o"],
                ["5 |oo.oo"]])
        return mapa

    elif nivel == 2:
        mapa = ([["  |ABCDE"],
                 ["1 |.o.o."],
                 ["2 |oo.oo"],
                 ["3 |.o.o."],
                 ["4 |o.o.o"],
                 ["5 |o.o.o"]])
        return mapa

    elif nivel ==3:
        mapa = ([["  |ABCDE"],
                 ["1 |o...o"],
                 ["2 |oo.oo"],
                 ["3 |..o.."],
                 ["4 |o.o.."],
                 ["5 |o.oo."]])
        return mapa

    elif nivel == 4:
        mapa = ([["  |ABCDE"],
                 ["1 |oo.oo"],
                 ["2 |....."],
                 ["3 |oo.oo"],
                 ["4 |....o"],
                 ["5 |oo..."]])
        return mapa

    elif nivel == 5:
        mapa = ([["  |ABCDE"],
                 ["1 |...oo"],
                 ["2 |...oo"],
                 ["3 |....."],
                 ["4 |oo..."],
                 ["5 |oo..."]])

        return mapa

print(mapaNivelPredeterminado(1))