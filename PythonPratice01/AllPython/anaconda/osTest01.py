# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:04:30 2019

@author: NEIL_YU
"""

import os

path=r"D:\PyAI2\MSO\XML"
filename=r"0_COCO_COCO_train2014_000000019391.xml"
filename_path=r"D:\PyAI2\MSO\XML\0_COCO_COCO_train2014_000000019391.xml"
testpath=r"D:\test\rphotos"
createdirspath=r"D:\test\createdirstest\test01"

print(os.sep)
print(os.path.normcase(path))
print(os.path.normpath(path))
print(os.path.normpath(path)+os.sep)
print(os.path.join(path,filename))
print(os.path.split(os.path.join(path,filename)))
print(os.walk(testpath))
print()
for i in os.walk(testpath):
    print(i)
    for it in i[2]:
        print(os.path.join(i[0],it))

print(os.path.basename(filename_path))
print(os.path.dirname(path))
print(os.path.splitext(filename_path))
print(os.path.splitext(os.path.basename(filename_path)))
print(os.path.getsize(filename_path))
#os.makedirs(createdirspath)
print(os.path.exists(createdirspath))