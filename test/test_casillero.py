import casillero
import unittest
from unittest.mock import patch

class casilleroTest(unittest.TestCase):

    mapaNivel1 = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']

    def testIngresoColumnaCoordenadaValidaDevuelveCoordenada(self):
        columnaCoordenada = "a"
        self.assertTrue(casillero.columnaCheck(columnaCoordenada,self.mapaNivel1))

    def testIngresoColumnaCoordenadaVaciaDevuelveFalso(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = ""
        self.assertFalse(casillero.columnaCheck(columnaCoordenada,mapa))

    def testIngresoColumnaCoordenadaEspacioDevuelveFalso(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = " "
        self.assertFalse(casillero.columnaCheck(columnaCoordenada,mapa))

    def testIngresaValorValidoDevuelveTrue(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = "a"
        resultado = casillero.columnaCheck(columnaCoordenada,mapa)
        self.assertEqual(resultado, True)

    def testIngresaCadenaDeCaracteresVaciaDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = ""
        resultado = casillero.columnaCheck(columnaCoordenada, mapa)
        self.assertEqual(resultado, False)

    def testIngresaColumnaInvalidaDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = "J"
        resultado = casillero.columnaCheck(columnaCoordenada, mapa)
        self.assertEqual(resultado, False)

    def testIngresaEnteroEnColumnaDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = 1
        resultado = casillero.columnaCheck(columnaCoordenada, mapa)
        self.assertEqual(resultado, False)

    def testIngresaNumeroComoStringEnColumnaDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        columnaCoordenada = "1"
        resultado = casillero.columnaCheck(columnaCoordenada, mapa)
        self.assertEqual(resultado, False)

    def testFilaCheckIngresaNumeroEnStringDevuelveTrue(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        filaCoordenada = "1"
        self.assertTrue(casillero.filaCheck(filaCoordenada, mapa))

    def testFilaCheckIngresaNumeroEnteroDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        filaCoordenada = 1
        self.assertFalse(casillero.filaCheck(filaCoordenada, mapa))

    def testFilaCheckIngresaVacioDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        filaCoordenada = ""
        self.assertFalse(casillero.filaCheck(filaCoordenada, mapa))

    def testFilaCheckIngresaEspacioDevuelveFalse(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        filaCoordenada = " "
        self.assertFalse(casillero.filaCheck(filaCoordenada, mapa))

    def testCoordenadaCheckIngresaVacioDevuelveTrue(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = ""
        self.assertTrue(casillero.coordenadaCheck(coordenada, mapa))

    def testCoordenadaCheckIngresaLetraSParaSalirDevuelveTrue(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = "S"
        self.assertTrue(casillero.coordenadaCheck(coordenada, mapa))

    def testCoordenadaCheckIngresaLetraSParaSalirDevuelveTrue(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = "s"
        self.assertTrue(casillero.coordenadaCheck(coordenada, mapa))

    def testCoordenadaCheckIngresaCoordenadaValidaDevuelveTrue(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = ("a","1")
        self.assertTrue(casillero.coordenadaCheck(coordenada, mapa))

    def testCoordenadaCheckIngresaCoordenadaColumnaInvalidaDevuelveMensajeError(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = ("J","1")
        mensaje = casillero.coordenadaCheck(coordenada, mapa)
        self.assertEqual(mensaje,"Ingrese correctamente el valor de la columna")

    def testCoordenadaCheckIngresaCoordenadaFilaInvalidaDevuelveMensajeError(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = ("a","10")
        mensaje = casillero.coordenadaCheck(coordenada, mapa)
        self.assertEqual(mensaje,"Ingrese correctamente el valor de la fila")

    def testCoordenadaCheckIngresaCoordenadaFilaYColumnaInvalidaDevuelveMensajeError(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        coordenada = ("W","1000")
        mensaje = casillero.coordenadaCheck(coordenada, mapa)
        self.assertEqual(mensaje,"Ingrese correctamente las coordenadas de columna y fila")


    def testIngresoCasillero(self):

        coordenada = ""

        self.assertEqual(casillero.validarCoordenada(coordenada),"")






