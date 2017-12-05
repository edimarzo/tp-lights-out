import casillero
import unittest
class casilleroTest(unittest.TestCase):
    def ingresoCoordenadaValidaDevuelveCoordenada(self):
        self.assertTrue(casillero.seleccionCasillero("a1"))