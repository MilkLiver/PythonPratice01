# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:58:47 2019

@author: NEIL_YU
"""


import numpy as np
import os
#import shutil
import re
import multiprocessing as mp
from multiprocessing.pool import ThreadPool
import threading 
import tkinter as tk

#路徑設定
XMLpath=r"D:\PyAI3\4\Annotation"
ImageSetdir=r"D:\PyAI3\4\ImageSet"
Maindir=r"D:\PyAI3\4\ImageSet\Main"
trainlist_name="train.txt"
testlist_name="test.txt"

#參數設定
threadNum=5
classifyNum=2

#變數
XMLFile_Names_dict={}
classify_name_pattern=re.compile("([A-Za-z0-9_]*)\s*[- R]*(\d*).xml")
classify_depuname_pattern=re.compile("(.*).xml")
txt_pattern=re.compile("(.*).txt")
traindataNum=0
testdataNum=0
window = tk.Tk()
tlock = threading.Lock()

def saveNewFile():
    global window,trainlist_name,testlist_name
    Maindirlist=os.listdir(Maindir)
    
    retrainlist_name=re.findall(txt_pattern,trainlist_name)[0]
    retestlist_name=re.findall(txt_pattern,testlist_name)[0]
    retrainlist_name+=".bak"
    retestlist_name+=".bak"
    
    repeatNum=1

    while retrainlist_name+str(repeatNum)+".txt" in Maindirlist:
        repeatNum+=1
    trainlist_name=retrainlist_name+str(repeatNum)+".txt"
    

    while retestlist_name+str(repeatNum)+".txt" in Maindirlist:
        repeatNum+=1
    testlist_name=retestlist_name+str(repeatNum)+'.txt'
    window.destroy()

def saveCoverFile():
    global window
    if os.path.exists(Maindir+"\\"+trainlist_name):
        os.remove(Maindir+"\\"+trainlist_name)
    if os.path.exists(Maindir+"\\"+testlist_name):
        os.remove(Maindir+"\\"+testlist_name)
    window.destroy()

def FileExistswarning():    
    
    window.title('Warning!!')
    window.geometry('270x150')

    l=tk.Label(
            window,
            text="檔案"+str(trainlist_name)+"或"+str(testlist_name)+"已存在\n是否要覆蓋當前檔案??",
            font=('Arial', 12),
            width=100, height=4)
    l.pack()

    YesBtn=tk.Button(window,
                     bg="white", 
                     text="是",
                     width=10, height=1,
                     command=saveCoverFile)
    
    NoBtn=tk.Button(window,
                    bg="white", 
                    text="否",
                    width=10, height=1,
                    command=saveNewFile)

    YesBtn.pack()
    NoBtn.pack()

    YesBtn.place(x=30,y=110)
    NoBtn.place(x=160,y=110)
    window.mainloop()

def Search(xml_name):
    global XMLFile_Names_dict
    XMLFile_re_Name=re.findall(classify_name_pattern,xml_name)[0]
    xml_dename=re.findall(classify_depuname_pattern,xml_name)[0]
    
    if XMLFile_re_Name[0] not in XMLFile_Names_dict:
        XMLFile_Names_dict[XMLFile_re_Name[0]]=[]
        
    XMLFile_Names_dict[XMLFile_re_Name[0]].append(xml_dename)
    

def SaveFile(xml_name,save_path):
    #print(xml_name)
    global tlock
    tlock.acquire()
    with open (Maindir+"\\"+save_path,'a') as td:
        for item in XMLFile_Names_dict[xml_name]:
            td.write(item+"\n")    
        #td.write("\n")
    tlock.release()
            
def resetDir():
    if not os.path.exists(ImageSetdir):
        os.makedirs(ImageSetdir)
        
    if not os.path.exists(Maindir):
        os.makedirs(Maindir)
        #shutil.rmtree(Maindir)
        
    trainexists=os.path.exists(Maindir+"\\"+trainlist_name)
    testexists=os.path.exists(Maindir+"\\"+testlist_name)
    if trainexists or testexists:
        FileExistswarning()
    else:
        window.destroy()
    print("train txt name: "+trainlist_name)
    print("test txt name: "+testlist_name)
        
    
def main():
    global testdataNum,traindataNum
    resetDir()
    #ml=mp.Manager().Lock()  
    #qu=mp.Manager().Queue()
    pool=ThreadPool(processes=threadNum)
    
    for i in os.listdir(XMLpath):
        pool.apply_async(Search,args=(i,))
        
    pool.close()
    pool.join()
    
    claNum=0
    
    pool=ThreadPool(processes=threadNum)
    for items in XMLFile_Names_dict:
        if claNum>2:
            testdataNum+=1
            claNum=0
            pool.apply_async(SaveFile,args=(items,testlist_name))
            
        else:
            traindataNum+=1
            claNum+=1
            pool.apply_async(SaveFile,args=(items,trainlist_name))
        
    
    pool.close()
    pool.join()
    #print(testdataNum,traindataNum)
    print("Finish!")

    
    



if __name__=="__main__":
    main()