# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:47:49 2019

@author: NEIL_YU
"""

import os

dirpath=r"D:\test\SelectedFileDir\cutImages"


dirpath=os.path.normpath(dirpath)
count=0

for i in os.walk(dirpath):
    for i2 in i[2]:
        count+=1
        
print(count)