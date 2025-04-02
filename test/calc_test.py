import unittest
from unittest.mock import patch
import xmlrunner

import sys

sys.path.append('src')

from calc import *

class TestCalculadora(unittest.TestCase):
    
    def testCalculadoraInstance(self):
        c = Calculadora()

        self.assertIsInstance(c, Calculadora)
        
    def testCalculadoraSomar(self):
        c = Calculadora()
        
        self.assertEqual(c.somar(5, 6), 11)

    def testCalculadoraSomarFail(self):
        c = Calculadora()
        
        self.assertNotEqual(c.somar(5, 6), 10.9999999)

    def testCalculadoraMult(self):
        c = Calculadora()
        
        self.assertEqual(c.multiplicar(5, 6), 30)

    def testCalculadoraMultFail(self):
        c = Calculadora()
        
        self.assertNotEqual(c.multiplicar(5, 6), 29.9999999)

    def testCalculadoraDivid(self):
        c = Calculadora()
        
        self.assertEqual(c.dividir(10, 2.5), 4)

    def testCalculadoraDividFail(self):
        c = Calculadora()
        
        self.assertNotEqual(c.dividir(10, 2.5), 4.0001)
    
    @patch('sys.stdout')  # Redireciona a saída do print 
    def testCalculadoraDividPorZero(self, mock_sdout):
        c = Calculadora()
        
        self.assertEqual(c.dividir(5, 0), None)

    def testCalculadoraPoten(self):
        c = Calculadora()
        
        self.assertEqual(c.potencia(4, 3), 64)

    def testCalculadoraPotenFail(self):
        c = Calculadora()
        
        self.assertNotEqual(c.potencia(4, 3), 64.00001)
        
if __name__ == '__main__':  
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), exit=False)
