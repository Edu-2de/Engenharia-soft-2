import unittest
from calculadora import somar, dividir

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2,3),5)
        self.assertEqual(somar(-1,1),0)
        self.assertEqual(somar(0,0),0)