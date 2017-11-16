def mapaNivelPredeterminado():
    """ Ingresa entero con número de nivel, devuelve mapa correspondiente a nivel."""
    #if a == 1:


    mapa = ([[" " ," ","A","B","C","D","E"],
            ["1" ," ","o","o",".","o","o"],
            ["2" ," ","o","o",".","o","o"]])
    for i, p in enumerate(mapa):
        print(i,p)
mapaNivelPredeterminado()