# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import caso1

class Test(unittest.TestCase):
    def test1(self):
        resultado = caso1.etiquetado_consumo_energia(25)
        self.assertEquals(resultado, "escala: A++ , eficiencia: los más eficientes")

if __name__ == '__main__':
    unittest.main()