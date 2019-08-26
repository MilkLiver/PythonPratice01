import multiprocessing  
import time

nu=0
num=[]
num.append(nu)

def sayHi(name):
    nu2=0
    num2=[]
    num2.append(nu2)
    while True:
        for i in num2:
            nu+=1
            num.append(nu2)

if __name__=='__main__':
    for i in num:
        nu+=1
        num.append(nu)
        p = multiprocessing.Process(target=sayHi, args=(i,))
        p.start()   

while True:
    pass
