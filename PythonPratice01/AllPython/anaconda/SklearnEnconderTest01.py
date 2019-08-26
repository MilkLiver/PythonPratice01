# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:18:46 2019

@author: NEIL_YU
"""

from sklearn import preprocessing,ensemble,metrics
import numpy as np

lab1=["OwO","OAO","OUO","OHO","OwO"]

le=preprocessing.LabelEncoder()
le.fit(lab1)

print(le.classes_)

lab2=le.transform(lab1)
print(lab2)

lab3=le.inverse_transform(lab2)
print(lab3)

rNum=np.random.randint(0,4,20)
print(rNum)


print(le.inverse_transform(rNum))
#==============================================================================
print("="*70)
