import niveles
import transformaMapa
import accion
import casillero

def modoJuegoAleatorio():
    """Modulo Juego en modo Aleatorio."""

    print("Bienvenido al modo aleatorio")

    cantidadDeNiveles = niveles.cantidadDeNivelesPredeterminado()
    puntaje = 0

    for numeroNivel in range(1, cantidadDeNiveles + 1):

        mapaNivel = niveles.mapaAleatorio()
        print("")
        print("Nivel {}".format(numeroNivel))
        print("")

        mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

        accion.muestraMapa(mapaNivelParaVisualizacion)

        contador = 0

        while True:
            contador = contador + 1
            coordenada = casillero.seleccionCasillero(mapaNivelParaVisualizacion)

            if coordenada == "":

                print("Reiniciar el tablero fueron {} puntos en contra".format(niveles.puntaje(mapaNivel,contador)))
                puntaje = puntaje + niveles.puntaje(mapaNivel,contador)
                print("Tu puntaje total es: {} puntos".format(puntaje))

                if puntaje < 0:
                    print("Te quedaste sin puntos! Hasta la próxima!")
                    break

                contador = 0
                mapaNivel = niveles.mapaAleatorio()
                mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

                print("Nivel {}".format(numeroNivel))
                print("")
                accion.muestraMapa(mapaNivelParaVisualizacion)

                continue
            elif coordenada == "s":
                break

            mapaNivel = transformaMapa.transformaMapa(coordenada, mapaNivel)
            mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

            accion.muestraMapa(mapaNivelParaVisualizacion)

            if mapaNivel == niveles.mapaAleatorioGanado(len(mapaNivel)):
                print("Felicitaciones ganaste el nivel {}!".format(numeroNivel))
                print("")
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)
                print("Tu puntaje en este nivel fue de +500 y tu puntaje total es: {}".format(puntaje))

                break
            elif contador == len(mapaNivel) * 3:
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)
                print("Te quedaste sin movimientos!")
                print("")
                print("Tu puntaje en este nivel fue de -300 y tu puntaje total es: {}".format(puntaje))

                if puntaje < 0:
                    print("Te quedaste sin puntos! Hasta la próxima!")
                    print("")
                    break

                break
        if coordenada == "s":
            break

        elif puntaje <0:
            print ("Te quedaste sin puntos! Hasta la próxima!")
            print("")
            break

    #print("Tu puntaje es: {}".format(puntaje))
    #for numeroNivel in range (1,cantidadDeNiveles+1):

