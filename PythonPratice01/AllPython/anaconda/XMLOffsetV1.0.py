# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:44:30 2019

@author: NEIL_YU
"""
from multiprocessing.pool import ThreadPool
#import threading 
import xml.dom.minidom
import xml.etree.ElementTree as ET
from PIL import Image
import re
import platform
import os
import sys
import time

#參數設定=============================================================
#XML資料夾路徑
xmldir_path=r"D:\PyAI\CarXml"
#Offset的XML路徑
new_xmldir_path=r"D:\PyAI\OffsetCarXml"
#未找到訊息的txt檔存放資料夾路徑
NotFoundImageXMLtxt_path=r"D:\PyAI"
#X座標offset值
x_offset=0
#y座標offset值
y_offset=0
#執行序數量
RthreadNum=30
#===================================================================

user_os=platform.system()
xml_img_name_pattren=re.compile(r'([^\\/]*).jpg')
NotFoundImageDict={}
NotFoundNumber=0
XMLTotalNumber=0
def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element


def XML_Offset(xml_name,x_offset=0,y_offset=0,osp="\\"):
    global XMLTotalNumber,NotFoundNumber
    doc=xml.dom.minidom.Document()
    root=doc.createElement('annotation')
    doc.appendChild(root)
    root.setAttribute('verified','yes')
    
    tree=ET.parse(xmldir_path+osp+xml_name)
    xmlroot=tree.getroot()
    #print(root.tag)
    rootChilds=[]
    xml_objects=[]
    for child in xmlroot:
        rootChilds.append(child)
        if child.tag=="object":
            xml_objects.append(child)
        
        
    #print(str(rootChilds[0].text))
    CreateElement(doc,root,'folder',str(rootChilds[0].text))
    CreateElement(doc,root,'filename',str(rootChilds[1].text))
    CreateElement(doc,root,'path',str(rootChilds[2].text))
    xml_source=CreateElement(doc,root,'source')
    CreateElement(doc,xml_source,'database',str(rootChilds[3][0].text))
    
    
    img_path=rootChilds[2].text
    if not os.path.exists(img_path):
        NotFoundNumber+=1
        img_name=re.findall(xml_img_name_pattren,img_path)[0]
        if img_name not in NotFoundImageDict:
            NotFoundImageDict[img_name]=[]
        NotFoundImageDict[img_name].append(xml_name)
        sys.exit()
        
    img=Image.open(img_path)
    
    img_width,img_height=img.size[0],img.size[1]
    #print(img_path)
    #print(img_width,img_height)
    
    #print(str(rootChilds[4][0].text))
    xml_img_size=CreateElement(doc,root,'size')
    CreateElement(doc,xml_img_size,'width',str(rootChilds[4][0].text))
    CreateElement(doc,xml_img_size,'height',str(rootChilds[4][1].text))
    CreateElement(doc,xml_img_size,'depth',str(rootChilds[4][2].text))
    
    CreateElement(doc,root,'segmented',str(rootChilds[5].text))
    
    for xml_object in xml_objects:
        objs=[]
        for items in xml_object:
            objs.append(items)
        
        obj=CreateElement(doc,root,'object')
        CreateElement(doc,obj,'name',str(objs[0].text))
        CreateElement(doc,obj,'pose',str(objs[1].text))
        CreateElement(doc,obj,'truncated',str(objs[2].text))
        CreateElement(doc,obj,'difficult',str(objs[3].text))
        xml_bndbox=CreateElement(doc,obj,'bndbox')
        xmin,ymin,xmax,ymax=[int(xml_axis.text) for xml_axis in objs[4]]
        #print(xmin,ymin,xmax,ymax)
        if xmin-x_offset<=0:
            xmin=1
            #os.exit()
        else:
            xmin-=x_offset
            
        if ymin-y_offset<=0:
            ymin=1
            #os.exit()
        else:
            ymin-=y_offset
            
        if xmax+x_offset>=img_width:
            xmax=img_width-1
            #os.exit()
        else:
            xmax+=x_offset
            
        if ymax+y_offset>=img_height:
            ymax=img_height-1
            #os.exit()
        else:
            ymax+=y_offset
            
        if xmin>xmax:
            xmin,xmax=xmax,xmin
        if ymin>ymax:
            ymin,ymax=ymax,ymin
            
        
        CreateElement(doc,xml_bndbox,"xmin",str(xmin))
        CreateElement(doc,xml_bndbox,"ymin",str(ymin))
        CreateElement(doc,xml_bndbox,"xmax",str(xmax))
        CreateElement(doc,xml_bndbox,"ymax",str(ymax))
        
    with open(new_xmldir_path+osp+xml_name,"w") as wxml:
        doc.writexml(wxml,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    
    XMLTotalNumber+=1
    #print(xml_name)

def saveNewFile(osp):
    global NotFoundImageXMLtxt_path
    New_Num=1
    while os.path.exists(NotFoundImageXMLtxt_path+osp+"NotFoundImageXML ("+str(New_Num)+").txt"):
        New_Num+=1
    NotFoundImageXMLtxt_path=NotFoundImageXMLtxt_path+osp+"NotFoundImageXML ("+str(New_Num)+").txt"

def saveCoverFile(osp):
    if os.path.exists(NotFoundImageXMLtxt_path+osp+"NotFoundImageXML.txt"):
        os.remove(NotFoundImageXMLtxt_path+osp+"NotFoundImageXML.txt")

def SaveDirCreate(osp):
    global NotFoundImageXMLtxt_path
    if not os.path.exists(new_xmldir_path):
        os.mkdir(new_xmldir_path)
    if os.path.exists(NotFoundImageXMLtxt_path+osp+"NotFoundImageXML.txt"):
        while True:
            decide=input("檔案NotFoundImageXML.txt已存在\n是否要覆蓋當前檔案??(y/n) ")
            if decide=="y" or decide=="yes"or decide=="Y" or decide=="Yes" or decide=="YES" or decide=="n" or decide=="no" or decide=="N" or decide=="No" or decide=="NO":
                break
        if decide=="y" or decide=="yes"or decide=="Y" or decide=="Yes" or decide=="YES":
            saveCoverFile(osp)
            NotFoundImageXMLtxt_path+=osp+"NotFoundImageXML.txt"
        if decide=="n" or decide=="no" or decide=="N" or decide=="No" or decide=="NO":
            saveNewFile(osp)
    else:
        NotFoundImageXMLtxt_path+=osp+"NotFoundImageXML.txt"

def systemPathSymbol():
    if user_os=="Windows":
        osp="\\"
    elif user_os=="Linux":
        osp="/"
    else:
        osp="/"
    return osp

def main():
    start_time=time.time()
    osp=systemPathSymbol()
    
    SaveDirCreate(osp)
    pool=ThreadPool(processes=RthreadNum)
    #progress=len(os.listdir(xmldir_path))
    #i=0
    
    print("starting")
    for xm in os.listdir(xmldir_path):
        #i+=1
        #pro=int(i/progress*100)
        #sys.stdout.write("\r[%-50s] %3d%%" % ('='*int(pro/2), pro))
        #sys.stdout.flush()
        pool.apply_async(XML_Offset,args=(xm,x_offset,y_offset,osp))
        
    pool.close()
    pool.join()
    
    
    with open(NotFoundImageXMLtxt_path,"a") as NFT:
        for img_name in sorted(NotFoundImageDict):
            NFT.write("未找到的圖片:"+str(img_name)+".jpg\n")
            NFT.write("未找到圖片的XML:")
            for img_path in sorted(NotFoundImageDict[img_name]):
                NFT.write(str(img_path)+",")
            NFT.write("\n\n")
            
            
    print("Txt Save Path:",NotFoundImageXMLtxt_path)
    print("XML Save Path:",new_xmldir_path)
    print("XML Total:",XMLTotalNumber)
    print("Not Found XML Image Total:",NotFoundNumber)
    print("Total use time: "+str(time.time()-start_time))
    print("finish")


if __name__=="__main__":
    main()



