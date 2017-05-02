import threading


class Controle:
    def __init__(self, n):
        self.list_size = n
        self.Estrutura = []
        self.ConsumeLock = threading.Lock()
        self.ProduceLock = threading.Lock()
        self.thirdLock = threading.Lock()

        self.consumidos = []
        self.consumidosLock = threading.Lock()

        self.ended_production = False

    def inserir(self, e, name):
        self.thirdLock.acquire(False)
        self.ProduceLock.acquire()   
        print(name + ' => Insert ' + str(e))

        if self.list_size == len(self.Estrutura):
            print('Full')            
            self.thirdLock.release()
            self.ProduceLock.acquire()

        self.Estrutura.append(e)
        print(name + ' => Inserted')
        print(str(self.Estrutura))
        self.ProduceLock.release()
    
    def remover(self, name):
        self.ConsumeLock.acquire()
        self.thirdLock.acquire()
        print(name+ ' => Take')
        
        if not len(self.Estrutura):
            print('Empty')
            if self.ended_production:
                self.thirdLock.release()
                self.ConsumeLock.release()
                return 'END'
            
            self.ProduceLock.release()
            self.thirdLock.acquire()
        
        value = self.Estrutura.pop(0)
        print(name + ' => Took ' + str(value))

        print(str(self.Estrutura))     
        self.thirdLock.release()
        self.ConsumeLock.release()
        return value

    def add_consumidos(self, e):
        self.consumidosLock.acquire()
        self.consumidos.append(e)
        # self.consumidos.sort()
        # print('_______' + str(self.consumidos) + '_______')
        self.consumidosLock.release()
