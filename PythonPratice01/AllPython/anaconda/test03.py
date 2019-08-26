# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 16:08:42 2019

@author: NEIL_YU
"""
import numpy as np



l1=[i for i in range(10)]
print(l1)
l2=(i for i in range(10))
print(list(l2))

t=[print(x) for x in range(20)]

#for i in l2:
#    print(i,end=' ')


dic={'a':1,'b':2,'c':3}
for i in dic:
    print(i,dic[i])
    
    
test01=np.arange(1,21).reshape(-1,4)
print(test01)
test02=np.array([])
for i in test02:
    print(i)