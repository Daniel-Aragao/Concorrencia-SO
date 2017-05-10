import threading
import random


class Producer(threading.Thread):
    def __init__(self, estrutura, number, n):
        super(Producer, self).__init__(name="Producer-"+str(number))
        self.name = "Producer-"+str(number)
        self.estrutura = estrutura
        self.elements = [(str(x)+'-P'+str(number)) for x in range(0, n)]
    
    def run(self):
        while self.elements:
            value = self.elements.pop(0)            
            self.estrutura.inserir(value, self.name)


class Consumer(threading.Thread):
    def __init__(self, estrutura, number):
        super(Consumer, self).__init__(name="Consumer-"+str(number))
        self.name = "Consumer-"+str(number)
        self.estrutura = estrutura
        self.elements = []
        self.value = 1
    
    def run(self):
        while self.value is not 'END':            
            self.value = self.estrutura.remover(self.name)

            if self.value is None:
                raise Exception("Value can't be None")
            
            if self.value is not 'END':
                self.elements.append(self.value)            
                self.estrutura.add_consumidos(self.value)
