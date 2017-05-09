import threading
import time
from ProducerConsumer import *
from Controle import Controle
from logger import Logger
from logger import LoggerFake


class Main:

    def __init__(self):
        self.estrutura = None

    def main_func(self, qtdP, qtdV, qtdC, n, log=Logger(), timeout=-1):
        self.estrutura = Controle(n, log, timeout=timeout)
        # log.daemon = True
        # log.start()

        prods = []
        consums = []

        for i in range(0, qtdP):
            p = Producer(self.estrutura, i, qtdV)
            # p.daemon = True
            p.start()
            prods.append(p)

        for i in range(0, qtdC):
            c = Consumer(self.estrutura, i)
            # c.daemon = True
            c.start()
            consums.append(c)

        consumed = 0
        producing = True

        while producing:
            producing = False
            for p in prods:
                if p.is_alive():
                    producing = True
        
        log.print('________Ended_production__________')
        self.estrutura.ended_production = True
        self.estrutura.thirdLock.release()

        while consumed < (qtdV * qtdP):
            consumed = 0
            for c in consums:
                consumed += len(c.elements)
        
        log.print("end => " + str(self.estrutura.consumidos))

        # if __name__ == '__main__':
        #     while True:
        #         pass


if __name__ == '__main__':
    qtdP = 20#int(input('Quantidade de produtores: '))
    qtdV = 4#int(input('Quantidade de valores por produtor: '))
    qtdC = 2#int(input('Quantidade de consumidores: '))
    n = 4#int(input('Tamanho da estrutura de dados: '))
    for i in range(1,20):
        Main().main_func(qtdP, qtdV, qtdC, n)  # , LoggerFake())
# else:
    # raise Exception('Must be main!')
