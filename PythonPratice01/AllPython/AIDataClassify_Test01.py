# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:00:25 2019

@author: NEIL_YU
"""

import numpy as np
import os
import shutil
import re
import multiprocessing as mp




XMLpath=r"D:\PyAI3\4\Annotation"

ImageSetdir=r"D:\PyAI3\4\ImageSet"
traindatadir=r"D:\PyAI3\4\ImageSet\Main\train"
trainlist_name="train.txt"
testdatadir=r"D:\PyAI3\4\ImageSet\Main\test"
testlist_name="test.txt"

processNum=3

def CopyFile(xml_name,traindatadir_path,testdatadir_path,mplock,mpqueue):
    mpqueue.put(xml_name)
        
            
def resetDir():
    if os.path.exists(ImageSetdir):
        shutil.rmtree(ImageSetdir)
        
    os.makedirs(ImageSetdir)
    os.makedirs(ImageSetdir+"\\"+"Main")
    os.makedirs(traindatadir)
    os.makedirs(testdatadir)
    
    if os.path.exists(traindatadir+"\\"+trainlist_name):
        os.remove(traindatadir+"\\"+trainlist_name)
    if os.path.exists(testdatadir+"\\"+testlist_name):
        os.remove(testdatadir+"\\"+testlist_name)
    
def main():
    resetDir()
    ml=mp.Manager().Lock()  
    qu=mp.Manager().Queue()
    pool=mp.Pool(processes=processNum)
    XMLFile_Names_dict={}
    
    for i in os.listdir(XMLpath):
        pool.apply_async(CopyFile,args=(i,traindatadir,testdatadir,ml,qu,))
        
    pool.close()
    pool.join()
    
    classify_name_pattern=re.compile('''\d*''')
    while not qu.empty():
        #XMLFile_Name.append(qu.get())
        XMLFile=qu.get()
        #print(type(class))
        te=re.findall(XMLFile,classify_name_pattern)
        print(te)
    #print(sorted(XMLFile_Name))

if __name__=="__main__":
    main()
