# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:49:04 2019

@author: NEIL_YU
"""

import numpy as np
import matplotlib.pyplot as mp
from scipy.optimize import fsolve
from math import cos


poi_num=5
#mp.figure()


x=np.arange(-poi_num,poi_num+1)
#mp.plot(x,y)
#mp.show()

def f(x):
    d = 140
    l = 156
    a = float(x[0])
    r = float(x[1])
    return [
        cos(a) - 1 + (d*d)/(2*r*r),
        cos(a) - 1 + (d*d)/(2*r*r)
    ]
result = fsolve(f, [1, 1])
print(result)