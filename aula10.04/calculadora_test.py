import unittest
from calculadora import somar, dividir

class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(1, 1), 2)

    def test_dividir(self):
        self.assertEqual(dividir(2, 0), 1)
        with self.assertRaises(ValueError):
            dividir(1, 0)

if __name__ == '__main__':
    unittest.main()
