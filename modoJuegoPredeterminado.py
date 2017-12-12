import niveles
import transformaMapa
import casillero
import accion
"""def modoJuegoPredeterminado():
    print("Bienvenido al modo predeterminado")

    cantidadDeNiveles = niveles.cantidadDeNivelesPredeterminado()

    for numeroNivel in range (1,cantidadDeNiveles+1):

        print("Nivel {}".format(numeroNivel))
        print("")

        mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
        mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(niveles.mapaNivelPredeterminado(numeroNivel))

        accion.muestraMapa(mapaNivelParaVisualizacion)
        contador = 0

        while True:
            contador = contador + 1
            coordenada = casillero.seleccionCasillero(niveles.mapaNivelPredeterminado(numeroNivel))
            if coordenada == "":
                contador = 0
                mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
                mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

                print("Nivel {}".format(numeroNivel))
                print("")
                accion.muestraMapa(mapaNivelParaVisualizacion)

                continue
            mapaNivelTransformado = transformaMapa.transformaMapa(coordenada, mapaNivel)
            mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivelTransformado)

            accion.muestraMapa(mapaNivelParaVisualizacion)

            if mapaNivelTransformado == niveles.mapaGanado:
                print("Felicitaciones ganaste el nivel {}".format(numeroNivel))
                print ("")
                break
            elif contador == len(mapaNivel)*3:
                print ("Te quedaste sin movimientos!")
                print("")
                break
            else:
                continue"""



def modoJuegoPredeterminado():
    print("Bienvenido al modo predeterminado")

    cantidadDeNiveles = niveles.cantidadDeNivelesPredeterminado()
    puntaje = 0

    for numeroNivel in range (1,cantidadDeNiveles+1):
        print("")
        print("Nivel {}".format(numeroNivel))
        print("")

        mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
        mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(niveles.mapaNivelPredeterminado(numeroNivel))

        accion.muestraMapa(mapaNivelParaVisualizacion)
        contador = 0

        while True:
            contador = contador + 1
            coordenada = casillero.seleccionCasillero(mapaNivelParaVisualizacion)

            if coordenada == "":
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)
                contador = 0
                mapaNivel = niveles.mapaNivelPredeterminado(numeroNivel)
                mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(niveles.mapaNivelPredeterminado(numeroNivel))

                print("Nivel {}".format(numeroNivel))
                print("")
                accion.muestraMapa(mapaNivelParaVisualizacion)

                continue

            elif coordenada == "s":
                break

            mapaNivel = transformaMapa.transformaMapa(coordenada, mapaNivel)
            mapaNivelParaVisualizacion = transformaMapa.transformadorDeMapa(mapaNivel)

            accion.muestraMapa(mapaNivelParaVisualizacion)

            if mapaNivel == niveles.mapaGanado:
                print("Felicitaciones ganaste el nivel {}!".format(numeroNivel))
                print ("")
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)
                print("Tu puntaje es: {}".format(puntaje))

                break
            elif contador == len(mapaNivel)*3:
                print ("Te quedaste sin movimientos!")
                print("")
                print("Tu puntaje es: {}".format(puntaje))
                puntaje = puntaje + niveles.puntaje(mapaNivel, contador)

                break
        if coordenada == "s":
            break