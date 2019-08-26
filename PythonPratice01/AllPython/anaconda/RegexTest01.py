# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:16:49 2019

@author: NEIL_YU
"""

import re


a=None
with open(r"D:\PyAI\NotFoundImageXML.txt","r") as txt:
    a=txt.read()

#print(a)
pattern=re.compile(r'([^\\/]*).jpg')
print(re.findall(pattern,a)[0])