import threading
import time


class Logger(threading.Thread):

    def __init__(self, on=True):
        super(Logger, self).__init__(name="Logger")
        self.fila = []    
        self.lock = threading.Lock()
        self.isOn = on
        
        # self.northgroup = PanedWindow(self.root)
        # Label(self.root, text="Clock").pack(side="left", padx=10)
        # self.button = button
    
    def print(self, msg):
        # self.lock.acquire()
        # self.fila.append(msg)
        print(msg)
        # self.lock.release()

    def run(self):
        
        while self.isOn:            
            # self.lock.acquire()
            if len(self.fila):
                print(self.fila.pop(0))
            # self.lock.release()
            time.sleep(0.4)        
    
    def setItOff(self):
        self.isOn = False


class LoggerFake(threading.Thread):

    def __init__(self, on=True):
        super(LoggerFake, self).__init__(name="LoggerFake")

    def print(self, msg):
        # self.lock.acquire()
        # self.fila.append(msg)
        # print(msg)
        # self.lock.release()
        pass

    def run(self):
        pass

    def setItOff(self):
        self.isOn = False