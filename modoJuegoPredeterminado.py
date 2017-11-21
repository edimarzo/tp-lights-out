import niveles
import transformaMapa
def modoJuegoPredeterminado():
    print("Bienvenido al modo predeterminado")

    for numeroNivel in range (1,6):

        print("Nivel {}".format(numeroNivel))

        mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
        mapaNivel = transformaMapa.transformadorDeMapa(mapaNivel)
        for linea in mapaNivel:
            print(linea)

        casilleroSeleccionado = input("Ingrese coordenada de casillero seleccionado")


modoJuegoPredeterminado()
