# Enter your code here. Read input from STDIN. Print output to STDOUT
from threading import Event, Thread, Timer
import random

data = []
data_to_get=10

class Server:
    def getData(self, callback, event):
        self.cb = callback
        self.event=event
        self.t = Timer(0.0005, self.dataReady)
        self.t.start()
        
    def dataReady(self):
        self.cb(random.random())
        self.event.set()


def ready(d):
    data.append(d)

def done():
    print data

def getData():
    theServer=Server()

    for i in range(data_to_get):
        event = Event()
        theServer.getData(ready, event)
        event.wait()

    done()

def someFunctionInsideMainThread():
    thread=Thread(target=getData)
    thread.start()