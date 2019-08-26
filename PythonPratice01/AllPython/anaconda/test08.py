# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:55:27 2019

@author: NEIL_YU
"""


try:
    print("test")
    try:
        a=int("test")
    except BaseException as err2:
        print("err2",err2)
    print("test2")
    int("OwO")
    
except BaseException as err:
    print("err1",err)