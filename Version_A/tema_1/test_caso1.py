import unittest
from Examen_test.Version_A.tema_1 import caso1

class Test(unittest.TestCase):
    def test1(self):
        resultado = caso1.etiquetado_consumo_energia(25)
        self.assertEquals(resultado, "escala: A++ , eficiencia: los más eficientes")

if __name__ == '__main__':
    unittest.main()