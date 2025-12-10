import threading
import time

respainast=threading.Semaphore(1)

def exmainationroom(num):
    print(f"patient {num} waiting of the turn")
    
    respainast.acquire()
    print(f"patient {num} on to the room")
    time.sleep(2)
    
    print(f"patient {num} out of the room")
    respainast.release()
    
patientlist=[] 
    
for i in range(10):
    patient=threading.Thread(target=exmainationroom,args=(i,))
    
    patientlist.append(patient)
    patient.start()
    
