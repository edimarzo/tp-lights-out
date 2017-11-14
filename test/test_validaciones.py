import unittest
import validaciones

class ValidacioensTest(unittest.TestCase):

    def testModoDeJuegoUnoDeberiaSerUnModoValido(self):
        self.assertTrue(validaciones.modoJuegoValido("1"))

    def testModoDeJuegoDosDeberiaSerUnModoValido(self):
        self.assertTrue(validaciones.modoJuegoValido("2"))

    def testModoDeJuegoSDeberiaSerUnModoValido(self):
        self.assertTrue(validaciones.modoJuegoValido("s"))

    def testModoDeJuegoVacioDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido(""))

    def testModoDeJuegoNumericoDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido(1))

    def testModoDeJuegoNoneDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido(None))

    def testModoDeJuegoListaDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido([]))

    def testModoDeJuegoListaConModoDeJuegoValidoDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido(["1"]))

    def testModoDeJuegoTuplaVaciaDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido(()))

    def testModoDeJuegoTuplaConModoDeJuegoValidoDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido(("1",)))

    def testModoDeJuegoDiccionarioConModoDeJuegoValidoDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido({"modoJuego":"1"}))

    def testModoDeJuegoDiccionarioConModoDeJuegoValidoDeberiaSerUnModoInvalido(self):
        self.assertFalse(validaciones.modoJuegoValido({}))