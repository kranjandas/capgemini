import threading
from threading import *
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("child thread")

t=MyThread()
t.start()
for i in range(1,6):
    print("Main Thread")