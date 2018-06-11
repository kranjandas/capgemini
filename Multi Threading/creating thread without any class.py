import threading
from threading import *
def display():
    print('This thread is executed by the (display function) thread',threading.current_thread().getName())

t=Thread(target=display)
t.start()
print('This thread is executed by the thread',threading.current_thread().getName())