import threading
import time
from ProducerConsumer import *
from Controle import Controle


def main_func():
    qtdP = int(input('Quantidade de produtores: '))
    qtdV = int(input('Quantidade de valores por produtor: '))
    qtdC = int(input('Quantidade de consumidores: '))
    n = int(input('Tamanho da estrutura de dados: '))
    estrutura = Controle(n)

    prods = []
    consums = []

    for i in range(0, qtdP):
        p = Producer(estrutura, i, qtdV)
        p.start()
        prods.append(p)

    for i in range(0, qtdC):
        c = Consumer(estrutura, i)
        c.start()
        consums.append(c)
    

    consumed = 0
    produced = 1

    while produced:
        produced = 0
        for p in prods:
            produced += len(p.elements)
    
    # print('________Ended_production__________')
    estrutura.ended_production = True
    estrutura.thirdLock.release()

    while consumed < (qtdV * qtdP):
        consumed = 0
        for c in consums:
            consumed += len(c.elements)
        
    for c in consums:
        print(str(c.getName()) + ' ended')
        c.join()
    
    for p in prods:
        print(str(p.getName()) + ' ended')
        p.join()
    
    print("end => " + str(estrutura.consumidos))


if __name__ == '__main__':
    main_func()
else:
    raise Exception('Must be main!')
