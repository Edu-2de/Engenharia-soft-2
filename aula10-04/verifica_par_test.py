import unittest
from verifica_par import verifica

class TestVerifica(unittest.TestCase):
    def test_verifica(self):
        self.assertTrue(verifica(2))     
        self.assertFalse(verifica(3))     
        self.assertTrue(verifica(0))      
        self.assertTrue(verifica(-4))     
if __name__ == '__main__':
    unittest.main()
