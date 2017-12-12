import casillero
import unittest
class casilleroTest(unittest.TestCase):
    def ingresoCoordenadaValidaDevuelveCoordenada(self):
        mapa = ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo']
        self.assertTrue(casillero.columnaCheck("a",mapa))