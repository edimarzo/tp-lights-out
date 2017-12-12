import menu
import modoJuegoAleatorio
import modoJuegoPredeterminado
import validaciones

def lightsout():

    while True:
        menu.mostrarMenu()
        modoJuego = menu.solicitarModoDeJuego()

        if validaciones.modoJuegoValido(modoJuego) == True :
            if modoJuego == "1":
                modoJuegoPredeterminado.modoJuegoPredeterminado()
            elif modoJuego == "2":
                modoJuegoAleatorio.modoJuegoAleatorio()
            elif modoJuego == "s":
                print("Nos vemos la próxima!")
                break
            else:
                print("El valor ingresado: "+modoJuego+ " es invalido. Elija una opcion valida")
                lightsout()

lightsout()