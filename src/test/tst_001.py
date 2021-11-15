import unittest


class Test_001 (unittest.TestCase):

    def setUp(self):
        pass

    def test_001(self):
        Variable_A = 6
        Variable_B = 4
        self.Resultado = Variable_A + Variable_B
        print(self.Resultado)

    def tearDown(self):
        self.assertTrue (self.Resultado == 10, "El valor no es 10, el valor es (self.Resultado)")



if __name__ == '__main__':
    unittest.main ()
