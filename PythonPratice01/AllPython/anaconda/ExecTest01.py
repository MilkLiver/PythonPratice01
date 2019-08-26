# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:47:45 2019

@author: NEIL_YU
"""


while True:
    try:
        inputexec=exec(input("input: "))
    except BaseException as ErrMsg:
        print(ErrMsg)
        break