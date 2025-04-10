import unittest
from verifica_par import verifica

class TestVerifica(unittest.TestCase):
    def test_verifica(self):
        self.assertEqual(verifica(2), True)
        self.assertEqual(verifica(3), False)
        self.assertEqual(verifica(0), True)
        self.assertEqual(verifica(-4), True)

if __name__ == '__main__':
    unittest.main()
