import niveles
import transformaMapa
import accion
import casillero

def modoJuegoAleatorio():
    print("Bienvenido al modo aleatorio")

    cantidadDeNiveles = niveles.cantidadDeNivelesPredeterminado()

    for numeroNivel in range(1, cantidadDeNiveles + 1):

        mapaNivel = niveles.mapaAleatorio()

        print("Nivel {}".format(numeroNivel))
        print("")

        mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

        accion.muestraMapa(mapaNivelParaVisualizacion)

        contador = 0

        while True:
            contador = contador + 1
            coordenada = casillero.seleccionCasillero(mapaNivelParaVisualizacion)

            if coordenada == "":
                contador = 0
                mapaNivel = niveles.mapaAleatorio()
                mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

                print("Nivel {}".format(numeroNivel))
                print("")
                accion.muestraMapa(mapaNivelParaVisualizacion)

                continue

            mapaNivel = transformaMapa.transformaMapa(coordenada, mapaNivel)
            mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

            accion.muestraMapa(mapaNivelParaVisualizacion)

            if mapaNivel == niveles.mapaAleatorioGanado(len(mapaNivel)):
                print("Felicitaciones ganaste el nivel {}".format(numeroNivel))
                print ("")
                break
            elif contador == len(mapaNivel)*3:
                print ("Te quedaste sin movimientos!")
                print("")
                break

    #for numeroNivel in range (1,cantidadDeNiveles+1):

modoJuegoAleatorio()