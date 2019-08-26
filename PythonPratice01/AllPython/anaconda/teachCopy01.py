# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:24:12 2019

@author: NEIL_YU
"""

import os
import shutil

target_path=r"c:\users\neil_yu\Desktop\ZT7000\test"
new_path=r"c:\users\neil_yu\Desktop\ZT7000\neww"

def copyFile(targetPath,newPath):
    targetList=os.listdir(targetPath)
    for i in targetList:
        if os.path.isdir(targetPath+"\\"+i):
            copyFile(targetPath+"\\"+i,newPath)
        else:
            shutil.copyfile(targetPath+"\\"+i,newPath+"\\"+i)

#copyFile(target_path,new_path)
shutil.copytree(target_path,new_path+"\\new")