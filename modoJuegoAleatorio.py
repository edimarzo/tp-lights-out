import niveles
import transformaMapa
import accion
import casillero

def modoJuegoAleatorio():
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
                puntaje = puntaje + niveles.puntaje(mapaNivel,contador)

                contador = 0
                mapaNivel = niveles.mapaAleatorio()
                mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

                print("Nivel {}".format(numeroNivel))
                print("")
                accion.muestraMapa(mapaNivelParaVisualizacion)

                continue
            if coordenada == "s":
                break

            mapaNivel = transformaMapa.transformaMapa(coordenada, mapaNivel)
            mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

            accion.muestraMapa(mapaNivelParaVisualizacion)

            if mapaNivel == niveles.mapaAleatorioGanado(len(mapaNivel)):
                print("Felicitaciones ganaste el nivel {}!".format(numeroNivel))
                print ("")
                print("Tu puntaje es: {}".format(puntaje))
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)

                break
            elif contador == len(mapaNivel)*3:
                print ("Te quedaste sin movimientos!")
                print("")
                print("Tu puntaje es: {}".format(puntaje))
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)
                break
        if coordenada == "s":
            break

    print("Tu puntaje es: {}".format(puntaje))
    #for numeroNivel in range (1,cantidadDeNiveles+1):

