import unittest
from builtins import staticmethod

from main import Main
from logger import LoggerFake


class Testing(unittest.TestCase):

    def test_passing_3p_4produts_2c_4length_return_not_empty_estructure(self):
        qtdP = 3
        qtdV = 4
        qtdC = 2
        n = 4
        programa = Main()
        programa.main_func(qtdP, qtdV, qtdC, n , LoggerFake())

        self.assertTrue(programa.estrutura.consumidos)

    # def test_passing_3p_4produts_2c_4length_return_allprodutcs(self):
    #     qtdP = 3
    #     qtdV = 4
    #     qtdC = 2
    #     n = 4
    #     programa = Main()
    #     programa.main_func(qtdP, qtdV, qtdC, n)  # , LoggerFake())

    #     self.assertTrue(Testing.assertProducts(programa, qtdP, qtdV))

    @staticmethod
    def assertProducts(programa, qtdp, qtdv):
        if len(programa.estrutura.consumidos) != qtdp * qtdv:
            return False
        
        for i in range(0, qtdp):
            for j in range(0, qtdv):
                if (str(j) + '-P' + str(i)) not in programa.estrutura.consumidos:
                    return False
        
        return True


if __name__ == '__main__':
    unittest.main()
