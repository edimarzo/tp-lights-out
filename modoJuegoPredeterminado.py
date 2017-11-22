import niveles
import transformaMapa
import casillero
def modoJuegoPredeterminado():
    print("Bienvenido al modo predeterminado")

    for numeroNivel in range (1,6):

        print("Nivel {}".format(numeroNivel))

        mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
        cuadricula = transformaMapa.transformadorDeMapa(mapaNivel)

        for linea in cuadricula:
            print(linea)

        casillero.seleccionCasillero()


modoJuegoPredeterminado()
