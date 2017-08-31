    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

import caso3
import caso4


class Test(unittest.TestCase):
    def test_caso3(self):
        resultado = caso3.premio_por_deposito_a_plazo_fijo(120, 50001)
        self.assertEquals(resultado, "Tipo de premio: mini nevera electrolux")

    def test_caso4(self):
        resultado = caso4.ofrecer_tarjeta_con_chip(20000 , "AAA" )
        self.assertEquals(resultado, "Tipo de tarjeta: Gold")

if __name__ == '__main__':
    unittest.main()