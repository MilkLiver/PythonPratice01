import multiprocessing  
import time

nu=0
num=[]
num.append(nu)
def sayHi(name):
    print ('Hi my name is',name)
    time.sleep(3)

if __name__=='__main__':
    for i in num:
        nu+=1
        num.append(nu)
        if nu == 20:
            break
        p = multiprocessing.Process(target=sayHi, args=(i,))
        p.start()   

while True:
    pass
