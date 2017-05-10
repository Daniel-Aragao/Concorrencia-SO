import threading
from logger import Logger


class Controle:
    def __init__(self, n, log: Logger(), timeout=2):
        self.wait_timeout = timeout
        self.list_size = n
        self.Estrutura = []

        self.condition = threading.Condition()
        self.consumidos = []
        self.consumidosLock = threading.Lock()

        self.ended_production = False

        self.log = log

    def inserir(self, e, name):
        self.condition.acquire()

        self.log.print(name + ' => Insert ' + str(e))

        while len(self.Estrutura) == self.list_size:
            self.log.print('full')
            self.log.print(name + ' going to sleep')
            self.condition.wait(self.wait_timeout)
            self.log.print(name + ' notified')

        self.Estrutura.append(e)
        self.log.print(name + ' => Inserted')
        self.condition.notify()
        self.condition.release()
        self.log.print(str(self.Estrutura))

    def remover(self, name):
        self.condition.acquire()

        self.log.print(name + ' => Take')

        while not len(self.Estrutura):
            if self.ended_production:
                self.log.print(name + ' ended')
                self.condition.notify()
                self.condition.release()
                return "END"
            self.log.print('empty')
            self.log.print(name + ' going to sleep')
            self.condition.wait(self.wait_timeout)
            self.log.print(name + ' notified')

        value = self.Estrutura.pop(0)

        self.log.print(name + ' => Took ' + str(value))
        self.condition.notify()
        self.condition.release()

        self.log.print(str(self.Estrutura))
        return value

    def add_consumidos(self, e):
        self.consumidosLock.acquire(timeout=self.wait_timeout)
        self.consumidos.append(e)
        # self.consumidos.sort()
        # self.log.print('_______' + str(self.consumidos) + '_______')
        self.consumidosLock.release()
