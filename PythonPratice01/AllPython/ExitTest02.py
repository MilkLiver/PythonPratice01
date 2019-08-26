import threading
import multiprocessing
import time
import os, sys


def ExitControl2():
    while True:
        try:
            time.sleep(1)
            print("I am running!")
            time.sleep(2)
            exit()
        except:
            break
    print("ExitControl2 exit~")
    exit()

def ExitControl():
    time.sleep(6)
    print("Exit")
    os._exit(0)
    #sys.exit(0)

def Child():
    count1=0
    while True:
        if count1>=5:
            print("Child Exit")
            #os._exit(0)
            sys.exit(0)
        count1+=1
        print("I am child")
        time.sleep(3)

def Parents():
    c1=threading.Thread(target=Child)
    #c2=threading.Thread(target=ExitControl)
    c3=threading.Thread(target=ExitControl2)
    #c1=multiprocessing.Process(target=Child)
    #c2=multiprocessing.Process(target=ExitControl)
    #c3=multiprocessing.Process(target=ExitControl2)
    
    c1.daemon=True
    #c2.daemon=True
    c3.daemon=True
    
    c1.start()
    #c2.start()
    c3.start()
    
    while True:
        print("I am parents")
        time.sleep(1)
        
    c1.join()
    #c2.join()
    c3.join()

if __name__=="__main__":
    Parents()
