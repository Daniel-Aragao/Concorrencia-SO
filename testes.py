import unittest
from builtins import staticmethod

from main import Main
from logger import LoggerFake
import time


class TestClass:
    pass


class Testing(unittest.TestCase):

    def test_passing_3p_4produts_2c_4length_return_not_empty_estructure(self):
        qtdP = 3
        qtdV = 4
        qtdC = 2
        n = 4
        programa = Main()
        programa.main_func(qtdP, qtdV, qtdC, n, log=LoggerFake())

        self.assertTrue(programa.estrutura.consumidos)

    def test_passing_3p_4produts_2c_4length_return_allprodutcs(self):
        qtdP = 3
        qtdV = 4
        qtdC = 2
        n = 4
        programa = Main()
        programa.main_func(qtdP, qtdV, qtdC, n, log=LoggerFake())

        self.assertTrue(Testing.assertProducts(programa, qtdP, qtdV)[0])

    def test_passing_10p_4produts_2c_4length_return_allprodutcs_stress(self):
        for i in range(0, 20):
            qtdP = 10
            qtdV = 4
            qtdC = 2
            n = 4
            programa = Main()
            programa.main_func(qtdP, qtdV, qtdC, n, timeout=1, log=LoggerFake())

            self.assertTrue(Testing.assertProducts(programa, qtdP, qtdV)[0])

    def test_passing_10p_100produts_9c_90length_return_allprodutcs_stress(self):
        test_result = True, None
        error_index = -1
        for i in range(0, 20):
            qtdP = 10
            qtdV = 100
            qtdC = 9
            n = 90
            programa = Main()
            programa.main_func(qtdP, qtdV, qtdC, n, timeout=1, log=LoggerFake())
            time.sleep(1)
            test_result = Testing.assertProducts(programa, qtdP, qtdV)
            if not test_result[0]:
                error_index = i
                break

        self.assertTrue(test_result)

    def test_assert_products_method_return_false_when_cant_find_the_elemen(self):
        qtdP = 10
        qtdV = 4

        programa = TestClass()
        programa.estrutura = TestClass()
        programa.estrutura.consumidos = [0 for i in range(0, qtdP * qtdV)]

        self.assertFalse(Testing.assertProducts(programa, qtdP, qtdV)[0])

    def test_assert_products_method_return_true_when_find_all_the_elemens(self):
        qtdP = 4
        qtdV = 4

        programa = TestClass()
        programa.estrutura = TestClass()
        programa.estrutura.consumidos = ['0-P0', '0-P1', '0-P2', '0-P3', '1-P0', '1-P1', '1-P2', '1-P3', '2-P0', '2-P1', '2-P2', '2-P3', '3-P0', '3-P1', '3-P2', '3-P3']

        self.assertTrue(Testing.assertProducts(programa, qtdP, qtdV)[0])

    @staticmethod
    def assertProducts(programa, qtdp, qtdv):
        if len(programa.estrutura.consumidos) != (qtdp * qtdv):
            return False, None
        
        for i in range(0, qtdp):
            for j in range(0, qtdv):
                if (str(j) + '-P' + str(i)) not in programa.estrutura.consumidos:
                    return False, i, j
        
        return True, None


if __name__ == '__main__':
    unittest.main()
