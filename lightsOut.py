import menu
import validaciones

def lightsout():

    menu.mostrarMenu()
    modoJuego = menu.solicitarModoDeJuego()

    if validaciones.modoJuegoValido(modoJuego):
        print("Super !!")
    else:
        print("El valor ingresado: "+modoJuego+ " es invalido. Elija una opcion valida")
        lightsout()

lightsout()