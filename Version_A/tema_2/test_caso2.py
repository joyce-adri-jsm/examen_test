# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import caso2

class Test(unittest.TestCase):
    def test1(self):
        resultado = caso2.clasificacion_clientes(45000 ,True)
        self.assertEquals(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

if __name__ == '__main__':
    unittest.main()