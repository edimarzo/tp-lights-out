import menu
import validaciones

def lightsout():

    menu.mostrarMenu()
    modoJuego = menu.solicitarModoDeJuego()

    if validaciones.modoJuegoValido(modoJuego) == True :
        if modoJuego == "1":
            print ("modo predeterminado")
        elif modoJuego == "2":
            print ("modo aleatorio")
        else:
            print("Nos vemos la próxima!")
    else:
        print("El valor ingresado: "+modoJuego+ " es invalido. Elija una opcion valida")
        lightsout()

lightsout()