import threading
import time
from ProducerConsumer import *
from Controle import Controle
from logger import Logger


class Main:

    def __init__(self):
        self.estrutura = None

    def main_func(self, qtdP, qtdV, qtdC, n, log=Logger()):
        estrutura = Controle(n, log)
        log.daemon = True
        log.start()

        prods = []
        consums = []

        for i in range(0, qtdP):
            p = Producer(estrutura, i, qtdV)
            # p.daemon = True
            p.start()
            prods.append(p)

        for i in range(0, qtdC):
            c = Consumer(estrutura, i)
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
        estrutura.ended_production = True
        estrutura.thirdLock.release()

        while consumed < (qtdV * qtdP):
            consumed = 0
            for c in consums:
                consumed += len(c.elements)
        
        log.print("end => " + str(estrutura.consumidos))


        if __name__ == '__main__':
            while True:
                pass


if __name__ == '__main__':
    qtdP = int(input('Quantidade de produtores: '))
    qtdV = int(input('Quantidade de valores por produtor: '))
    qtdC = int(input('Quantidade de consumidores: '))
    n = int(input('Tamanho da estrutura de dados: '))
    Main().main_func(qtdP, qtdV, qtdC, n)
# else:
    # raise Exception('Must be main!')
