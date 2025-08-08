# Exemplo básico usando unittest
import unittest

class TestAdicao(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(2 + 2, 4)

    def test_soma_negativos(self):
        self.assertEqual(-2 + (-2), -4)

if __name__ == '__main__':
    unittest.main()
