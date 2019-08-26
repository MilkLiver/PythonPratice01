# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:23:47 2019

@author: NEIL_YU
"""

def test(*arg):
    print(type(arg))
    print(arg)
    print(arg[0])
    print(*arg)
    
test([1,2,3,4,5])
print(*([5,6,7],))
print(*[[1,2,3]])