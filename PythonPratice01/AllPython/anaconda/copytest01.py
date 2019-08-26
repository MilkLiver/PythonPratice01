# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:05:04 2019

@author: NEIL_YU
"""

import numpy as np
import os
import shutil
import re



path=r"c:\users\neil_yu\Desktop\ZT7000\test"
newpath=r"c:\users\neil_yu\Desktop\ZT7000\neww"

way="c" #way裡面輸入  m-->移動 c-->複製
path+="\\"
newpath+="\\"

def CopyFile(dirpath,newdirpath):
    def SameFileCopy(filename):
        same_pattern=re.compile("複製")
        if re.findall(same_pattern,filename) != []:
            sameNum_pattern=re.compile("複製_\((\d+)\)")
            Copynum=re.findall(sameNum_pattern,filename)
            #print("OwO:",re.findall(sameNum_pattern,filename))
            if Copynum!=[]:
                copyname_pattern=re.compile("複製_\(*\d*\)*\s*(.*)")
                filename=re.findall(copyname_pattern,filename)[0]
                #print("OAO:",re.findall(sameNum_pattern,filename))
                return "複製_("+str(int(Copynum[0])+1)+") "+filename
            copyname_pattern=re.compile("複製_(.*)")
            filename=re.findall(copyname_pattern,filename)[0]
            #print("test2")
            return "複製_("+str(1)+") "+filename
        return "複製_"+filename
        #if newpath
        
    for i in os.listdir(dirpath):
        if os.path.isdir(dirpath+i):
            CopyFile(dirpath+i+"\\",newdirpath)
        else:
            if os.path.exists(newdirpath+i):
                shutil.copyfile(dirpath+i,newdirpath+SameFileCopy(i))
                continue
            shutil.copyfile(dirpath+i,newdirpath+i)

def MoveFile(dirpath,newdirpath):
    def SameFileCopy(filename):
        same_pattern=re.compile("複製")
        if re.findall(same_pattern,filename) != []:
            sameNum_pattern=re.compile("複製_\((\d+)\)")
            Copynum=re.findall(sameNum_pattern,filename)
            #print("OwO:",re.findall(sameNum_pattern,filename))
            if Copynum!=[]:
                copyname_pattern=re.compile("複製_\(*\d*\)*\s*(.*)")
                filename=re.findall(copyname_pattern,filename)[0]
                #print("OAO:",re.findall(sameNum_pattern,filename))
                return "複製_("+str(int(Copynum[0])+1)+") "+filename
            copyname_pattern=re.compile("複製_(.*)")
            filename=re.findall(copyname_pattern,filename)[0]
            #print("test2")
            return "複製_("+str(1)+") "+filename
        return "複製_"+filename
        #if newpath
        
    for i in os.listdir(dirpath):
        if os.path.isdir(dirpath+i):
            MoveFile(dirpath+i+"\\",newdirpath)
        else:
            if os.path.exists(newdirpath+i):
                shutil.move(dirpath+i,newdirpath+SameFileCopy(i))
                continue
            shutil.move(dirpath+i,newdirpath+i)
            
if way=="m":
    MoveFile(path,newpath)
if way=="c":
    CopyFile(path,newpath)

print("finish!!")

