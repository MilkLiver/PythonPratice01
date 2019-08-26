# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:26:15 2019

@author: NEIL_YU
"""

import numpy as np


def fun01(n):
    l1=[]
    l2=[]
    for i in range(1,n+1):
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
            
    return l1,l2


def fun02(n):
    l1=[]
    l2=[]
    for i in range(1,n+1):
        if i%2==0:
            l1.append(i)
        else:
            l2.append(i)
            
    return l1,l2
     
a,b=fun01(10)
    
for n1,n2 in zip(*fun01(10)):
    print(n1,n2)
    
print("-"*50)
    
for n in [n1 for n1 in fun01(10)]:
    print('n:',n)
    #print(n2)
    
print("-"*50)
 
for n1 in enumerate(fun02(10)):
    print(n1)

t1=[n1 for n1 in fun02(10)]
print(t1)

#print(a,b)
#print(*fun01(10))   
#print(*fun01(10))

    
    
    
#print(fun01(7))


print('-'*50)

a=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(2,5)
print(a)

for x,y in zip(*a):
    print(x,y)