from multiprocessing import *
import time


def fun1(name="OwO"):
    print("test")
    n=0
    while True:
        if n>=10:
            break
        else:
            time.sleep(2)
            print(name)
            n+=1
        

def fun2(name="OAO"):
    print("test")
    n=0
    while True:
        if n>=10:
            break
        else:
            time.sleep(3)
            print(name)
            n+=1

if __name__=="__main__":
    p1=Process(target=fun1,args=("process1",))
    p2=Process(target=fun2,args=("process2",))

    p1.daemon=True
    p2.daemon=True
    
    p1.start()
    p2.start()
    print("start")
    p1.join()
    p2.join()
    print("end")
