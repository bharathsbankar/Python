#by default execution uses main thread

from threading import Thread
from time import sleep

class Brake(Thread):
    def __init__(self, str):
        self.str = str
        super().__init__()


    def run(self):
        for i in range(5):
            print(self.str)
            sleep(1)

class Clutch(Thread):
    def __init__(self,str):
        self.str=str
        super().__init__()

    def run(self):
        for i in range(5):
            print(self.str)
            sleep(1)
a=Clutch("a thread")
b=Brake("b thread")
print("main thread")
#implicitly start() invokes run() of the class
# a thread is created as a branch from main thread and it starts to execute parallely
a.start()
sleep(.1)
#another b thread is created as a branch from main thread and it starts to execute parallely
b.start()
#main thread starts to execute the remaining statements
#in order to make main thread wait till the others thread complete their execution join() method is used
a.join()
b.join()
print("main thread resumes")



