#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import JuegoAdivinemosNumeros

NUMTEST = 10

class TestJuegoAdivinemosNumeros(unittest.TestCase):

#Test del Proceso para adivinar el número del Robot
    def testGuessRobotNumber(self):
        self.assertEqual(JuegoAdivinemosNumeros.guessRobotNumber(),NUMTEST)

#Test del Proceso para que el Robot adivine el número del Usuario 
    def testGuessUserNumber(self):
        self.assertEqual(JuegoAdivinemosNumeros.guessUserNumber(),NUMTEST)

#Test de la Función para validar que se ingresen enteros
    def testValidOption(self):
        self.assertEqual(JuegoAdivinemosNumeros.validOption(0),NUMTEST)

#Test de la Función para consultar a Usuario si desea jugar nuevamente
    def testPlayAgain(self):
        self.assertTrue(JuegoAdivinemosNumeros.playAgain())

unittest.main()