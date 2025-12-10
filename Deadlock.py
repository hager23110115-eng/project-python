import threading
import time

resource_1=threading.Lock()
resource_2=threading.Lock()

def thread_1():
    with resource_1:
        print("thread 1 acquire resource_1")
        time.sleep(2)
        print("thread 1 waiting resource_2")
    with resource_2:
        print("thread 1 acquire resource_2 complete ")
        
def thread_2():
    with resource_2:
        print("thread 2 acquire resource_2")
        time.sleep(2)
        print("thread 2 waiting resource_1")
        with resource_1:
             print("thread 2 acquire resource_1 complete ")
        
a=threading.Thread(target=thread_1)
b=threading.Thread(target=thread_2)

a.start()
b.start()
        
                
