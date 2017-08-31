# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

import caso1
import caso2


class Test(unittest.TestCase):
    def test_caso1(self):
        resultado = caso1.etiquetado_consumo_energia(25)
        self.assertEquals(resultado, "escala: A++ , eficiencia: los más eficientes")

    def test_caso2(self):
        resultado = caso2.clasificacion_clientes(45000 ,True)
        self.assertEquals(resultado, "Tipo de cliente: AAA, Envio de boletin: Si")

if __name__ == '__main__':
    unittest.main()