import unittest
import transformaMapa

class transformaMapaTest(unittest.TestCase):
    def ingresaMapaNivel1DevuelveMapaNuevoNivel1(self):
        n = [["o", "o", ".", "o", "o"],
          ["o", ".", "o", ".", "o"],
          [".", "o", "o", "o", "."],
          ["o", ".", "o", ".", "o"],
          ["o", "o", ".", "o", "o"]]
        resultado = transformaMapa.transformadorDeMapa(n)
        self.assertEqual(resultado, ['  |ABCDE', '1 |oo.oo', '2 |o.o.o', '3 |.ooo.', '4 |o.o.o', '5 |oo.oo'])

    def ingresaMapaNivel2DevuelveMapaNuevoNivel2(self):
        n = [[".", "o", ".", "o", "."],
          ["o", "o", ".", "o", "o"],
          [".", "o", ".", "o", "."],
          ["o", ".", "o", ".", "o"],
          ["o", ".", "o", ".", "o"]]
        resultado = transformaMapa.transformadorDeMapa(n)
        self.assertEqual(resultado, ['  |ABCDE', '1 |.o.o.', '2 |oo.oo', '3 |.o.o.', '4 |o.o.o', '5 |o.o.o'])