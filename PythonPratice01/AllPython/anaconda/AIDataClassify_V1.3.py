# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:58:47 2019

@author: NEIL_YU
"""


#import numpy as np
import os
import re
#import multiprocessing as mp
from multiprocessing.pool import ThreadPool
import threading 
#import tkinter as tk

#路徑設定
XMLpath=r"D:/PyAI3/4/Annotation"
ImageSetdir=r"D:/PyAI3/4/ImageSet"
Maindir=r"D:\PyAI3\4\ImageSet\Main"
trainlist_name="train.txt"
testlist_name="test.txt"

#參數設定
RthreadNum=5 #讀取的執行緒數量
WthreadNum=1 #寫入的執行緒數量 ＊若設定數量為1個以上 txt檔中的組的順序有可能會發生順序亂掉 
classifyNum=[2,1] #[train數量,test數量]

#變數
XMLFile_Names_dict={}
classify_name_pattern=re.compile("([A-Za-z0-9_]*)[- R]*(\d*).xml")
classify_depuname_pattern=re.compile("(.*).xml")
txt_pattern=re.compile("(.*).txt")
traindataNum=0
traindata_items_total=0
testdata_items_total=0
testdataNum=0
#window = tk.Tk()
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

def saveCoverFile():
    global window
    if os.path.exists(Maindir+"\\"+trainlist_name):
        os.remove(Maindir+"\\"+trainlist_name)
    if os.path.exists(Maindir+"\\"+testlist_name):
        os.remove(Maindir+"\\"+testlist_name)

def FileExistswarning():    
    decide=""
    while True:
        decide=input("檔案"+str(trainlist_name)+"或"+str(testlist_name)+"已存在\n是否要覆蓋當前檔案??(y/n) ")
        if decide=="y" or decide=="yes"or decide=="Y" or decide=="Yes" or decide=="YES" or decide=="n" or decide=="no" or decide=="N" or decide=="No" or decide=="NO":
            break
    if decide=="y" or decide=="yes"or decide=="Y" or decide=="Yes" or decide=="YES":
        saveCoverFile()
    if decide=="n" or decide=="no" or decide=="N" or decide=="No" or decide=="NO":
        saveNewFile()
        

def Search(xml_name):
    global XMLFile_Names_dict
    XMLFile_re_Name=re.findall(classify_name_pattern,xml_name)[0]
    xml_dename=re.findall(classify_depuname_pattern,xml_name)[0]
    
    if XMLFile_re_Name[0] not in XMLFile_Names_dict:
        XMLFile_Names_dict[XMLFile_re_Name[0]]=[]
        
    XMLFile_Names_dict[XMLFile_re_Name[0]].append(xml_dename)
    

def SaveFile(xml_name,save_path,data_type):
    #print(xml_name)
    global tlock,traindata_items_total,testdata_items_total
    tlock.acquire()
    #print(xml_name)
    with open (Maindir+"\\"+save_path,'a') as td:
        for item in sorted(XMLFile_Names_dict[xml_name]):
            if data_type=="train":
                traindata_items_total+=1
            else:
                testdata_items_total+=1
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
        
    print("train txt name: "+trainlist_name)
    print("test txt name: "+testlist_name)
        
    
def main():
    global testdataNum,traindataNum
    resetDir()
    pool=ThreadPool(processes=RthreadNum)
    
    for i in os.listdir(XMLpath):
        pool.apply_async(Search,args=(i,))
        
    pool.close()
    pool.join()
    
    trainNum=0
    testNum=0
    pool=ThreadPool(processes=WthreadNum)
    for items in sorted(XMLFile_Names_dict):
        if trainNum==classifyNum[0]:
            #print(items)
            testdataNum+=1
            pool.apply_async(SaveFile,args=(items,testlist_name,"test"))
            testNum+=1
            if testNum==classifyNum[1]:
                testNum=0
                trainNum=0
            
        else:
            #print(items)
            traindataNum+=1
            trainNum+=1
            pool.apply_async(SaveFile,args=(items,trainlist_name,"train"))
        
    
    pool.close()
    pool.join()
    #print(testdataNum,traindataNum)
    print("train teams total : "+str(traindataNum)+" items total : "+str(traindata_items_total))
    print("test teams total : "+str(testdataNum)+" items total : "+str(testdata_items_total))
    print("total teams : "+str(traindataNum+testdataNum)+" total items : "+str(traindata_items_total+testdata_items_total))
    print("Finish!")

    
    



if __name__=="__main__":
    main()