"""
Given an integer, N, perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
"""


from aula1 import par_impar

import unittest

class MyTest(unittest.TestCase):
    def teste_par_impar_recebe_3_espera_impar(self):
        self.assertEqual(par_impar(3), "Weird")

    def teste_par_impar_recebe_2_espera_par(self):
        self.assertEqual(par_impar(2), "Not Weird")

    def teste_par_impar_recebe_4_espera_par(self):
        self.assertEqual(par_impar(4), "Not Weird")

    def teste_par_impar_recebe_5_espera_impar(self):
        self.assertEqual(par_impar(5), "Weird")

    def teste_par_impar_recebe_6_espera_par(self):
        self.assertEqual(par_impar(6), "Weird")

    def teste_par_impar_recebe_7_espera_impar(self):
        self.assertEqual(par_impar(7), "Weird")

    def teste_par_impar_recebe_20_espera_weird(self):
        self.assertEqual(par_impar(20), "Weird")

    def teste_par_impar_recebe_21_espera_weird(self):
        self.assertEqual(par_impar(21), "Weird")

    def teste_par_impar_recebe_22_espera_not_weird(self):
        self.assertEqual(par_impar(22), "Not Weird")