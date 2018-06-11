#import threading
from threading import *
def display():
    for i in range(10):
        print("Child Thread")

t=Thread(target=display)
t.start()
for i in range(2,15):
    print("Main Thread")