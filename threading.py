import threading
import time

def task_1():
    print("starting of thread",threading.current_thread().name)
    time.sleep(2)
    print("finish of thread",threading.current_thread().name)
    
def task_2():
    print("starting of thread",threading.current_thread().name)
    print("finish of thread",threading.current_thread().name)
    
def task_3():
    print("starting of thread",threading.current_thread().name)
    time.sleep(2)
    print("finish of thread",threading.current_thread().name)
    
a=threading.Thread(target=task_1,name="thread 1")   
b=threading.Thread(target=task_2,name="thread 2")
c=threading.Thread(target=task_3,name="thread 3")

a.start()
b.start()
c.start()
 
