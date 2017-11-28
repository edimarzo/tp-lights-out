import niveles
import transformaMapa
import casillero
def modoJuegoPredeterminado():
    print("Bienvenido al modo predeterminado")

    cantidadDeNiveles = niveles.cantidadDeNivelesPredeterminado()

    for numeroNivel in range (1,cantidadDeNiveles+1):

        print("Nivel {}".format(numeroNivel))
        print("")

        mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)

        transformaMapa.displayMapa(mapaNivel)

        coordenada = casillero.seleccionCasillero()

        """Con la coordenada necesito decodificarla de manera de localizar esa ubicación en el mapa"""
        """Necesito crear la función que prenda y apague los casilleros"""
        print(coordenada)


modoJuegoPredeterminado()
