import threading
from logger import Logger


class Controle:
    def __init__(self, n, log: Logger(), timeout=-1):
        self.wait_timeout = timeout
        self.list_size = n
        self.Estrutura = []
        self.ConsumeLock = threading.Lock()
        self.ProduceLock = threading.Lock()
        self.thirdLock = threading.Lock()

        self.consumidos = []
        self.consumidosLock = threading.Lock()

        self.ended_production = False

        self.log = log

    def inserir(self, e, name):
        self.thirdLock.acquire(False)
        self.ProduceLock.acquire(timeout=self.wait_timeout)
        self.log.print(name + ' => Insert ' + str(e))

        if self.list_size == len(self.Estrutura):
            self.log.print('Full')            
            self.thirdLock.release()
            self.ProduceLock.acquire(timeout=self.wait_timeout)

        self.Estrutura.append(e)
        self.log.print(name + ' => Inserted')
        self.log.print(str(self.Estrutura))
        self.ProduceLock.release()
    
    def remover(self, name):
        self.ConsumeLock.acquire(timeout=self.wait_timeout)
        self.thirdLock.acquire(timeout=self.wait_timeout)
        self.log.print(name + ' => Take')
        
        if not len(self.Estrutura):
            self.log.print('Empty')
            if self.ended_production:
                self.thirdLock.release()
                self.ConsumeLock.release()
                return 'END'
            
            self.ProduceLock.release()
            self.thirdLock.acquire(timeout=self.wait_timeout)
        
        value = self.Estrutura.pop(0)
        self.log.print(name + ' => Took ' + str(value))

        self.log.print(str(self.Estrutura))     
        self.thirdLock.release()  # 3 5 4 7
        self.ConsumeLock.release()
        return value

    def add_consumidos(self, e):
        self.consumidosLock.acquire(timeout=self.wait_timeout)
        self.consumidos.append(e)
        # self.consumidos.sort()
        # self.log.print('_______' + str(self.consumidos) + '_______')
        self.consumidosLock.release()
