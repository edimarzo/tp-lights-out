import niveles
import transformaMapa
import casillero
def modoJuegoPredeterminado():
    print("Bienvenido al modo predeterminado")

    for numeroNivel in range (1,6):

        print("Nivel {}".format(numeroNivel))
        """Revisar si es posible que directamente muestre el mapa transformado. """
        mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
        mapaTransformado = transformaMapa.transformadorDeMapa(mapaNivel)

        for linea in mapaTransformado:
            print(linea)

        """Tratar de meter todo el ciclo while en funcion seleccion de casillero de manera que sólo permanezca acá la selección del casillero"""
        coordenada = casillero.seleccionCasillero()
        a = casillero.coordenadaCheck(coordenada, mapaTransformado)
        while a != "Coordenada Ok":
            print(a)
            coordenada = casillero.seleccionCasillero()
            a == casillero.coordenadaCheck(coordenada, mapaTransformado)
            if a != "Coordenada Ok":
                break
            else:
                continue
        """Con la coordenada necesito decodificarla de manera de localizar esa ubicación en el mapa"""
        """Necesito crear la función que prenda y apague los casilleros"""
        print(coordenada)


modoJuegoPredeterminado()
