import unittest


class tst_002 (unittest.TestCase):

    def SetUp(self):
        pass

    def test_002(self):
        self.Variable_A = 6
        self.Variable_B = 6
        self.Resultado = self.Variable_A + self.Variable_B
        #dfsdfsdf
        self.assertEqual (self.Variable_A, self.Variable_B, "Son iguales")

    def test_003(self):
        self.Variable_A = 6
        self.Variable_B = 7
        self.Resultado = self.Variable_A + self.Variable_B

        self.assertNotEqual (self.Variable_A, self.Variable_B, "no Son iguales")

    def test_004(self):
        self.Variable_A = 50

        if self.Variable_A >= 10:
            self.Resultado = True
        else:
            self.Resultado = False
        self.assertTrue (self.Resultado, f"no es tru es:{self.Variable_A}")

    def test_005(self):
        self.Variable_A = "Bienvenido a la clase de Unittest"
        self.Variable_B = "Unittest"

        self.assertIn (self.Variable_B, self.Variable_A, "No coinciden")

    def tearDown(self):
        pass


# constructor
if __name__ == '__main__':
    unittest.main ()
