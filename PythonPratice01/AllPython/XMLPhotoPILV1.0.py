# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:48:37 2019

@author: NEIL_YU
"""

from multiprocessing.pool import ThreadPool
import xml.dom.minidom
import xml.etree.ElementTree as ET
from PIL import Image
import os
import sys
import time
#import cv2
import shutil
#import numpy as np

#參數設定=============================================================
#XML來源資料夾路徑
xmldir_path=r"D:\PyAI4\VOCdevkit\VOC2012\Annotations"
#圖片來源資料夾路徑
imagedir_path=r"D:\PyAI4\VOCdevkit\VOC2012\JPEGImages"

#裁切圖片功能 y or n
cutFunctionOption="y"
#生成XML功能 y or n
createXMLFunctionOption="n"

#裁切後的圖片資料夾路徑
cutImage_dir_path=r"D:\test\SelectedFileDir\cutImages"
#更改後的XML資料夾路徑
NewXML_dir_path=r"D:\test\SelectedFileDir\SelectedXML"
#挑選到的圖片資料夾儲存路徑
image_SaveDir_path=r"D:\test\SelectedFileDir\SelectedImage"
#圖檔格式
imageformat=r".jpg"
#執行緒數量
threadpool_num=3
#XML未找到圖片的錯誤訊息txt檔路徑
NotFoundImagetxt_path=r"D:\test\SelectedFileDir"
#XML未找到圖片的錯誤訊息txt檔名稱
NotFoundImagetxt_name=r"NotFoundImage.txt"
#圖片質量 1~100
img_quality=95
#指定的classes 不指定 classes=""
classes="bus,car,motorbike,person"
#將要進行改名的類別更改名稱  classes_changeName={"要更改的類別名":"更改的類別名稱"} 若不更改:classes_changeName={}
classes_changeName={"motorbike":"moto"}

#===================================================================
classes=classes.split(",")
Rinput_XML_num=0
Winput_XML_num=0
Routput_CutImage_num=0
Woutput_CutImage_num=0
output_CutImage_type=set()
NotFoundImagetxt_dict={}
image_compression_para=[]
#===================================================================
def axisCheck(xmin,ymin,xmax,ymax,image_size):
    
    if xmin>xmax:
        xmin,xmax=xmax,xmin
        
    if ymin>ymax:
        ymin,ymax=ymax,ymin
        
    if xmin<=0:
        xmin=1
        
    if ymin<=0:
        ymin=1
        
    if xmax>=image_size[0]:
        xmax=image_size[0]-1
        
    if ymax>=image_size[1]:
        ymax=image_size[1]-1
    
    return xmin,ymin,xmax,ymax
    

def CreateCutImage(xmin,ymin,xmax,ymax,name,image_path,image_type=None,img_num=0):
    img=Image.open(image_path)
    xmin,ymin,xmax,ymax=axisCheck(xmin,ymin,xmax,ymax,img.size)
    img2=img.crop((xmin,ymin,xmax,ymax))
    img2.save(os.path.join(os.path.join(cutImage_dir_path,image_type),name),quality=img_quality)

def CopyOrMoveXML(xml_path,xml_Savepath,behavior):
    if behavior in ["c","copy","C","COPY","Copy"]:
        shutil.copy(xml_path,xml_Savepath)
                
    if behavior in ["m","move","M","MOVE","Move"]:
        shutil.move(xml_path,xml_Savepath)

def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element

def CreateNewXML(xml_name):
    global Winput_XML_num,Woutput_CutImage_num
    xml_objects_num=0
    try:
        xml_tree=ET.parse(os.path.join(xmldir_path,xml_name))
        Winput_XML_num+=1
        def searchAllChilds(read_parent,write_parent):
            nonlocal doc,xml_objects_num
            for child in read_parent:
                if child.tag=="object":
                    if child.find("name").text not in classes:
                        continue
                    xml_objects_num+=1
                        
                if [i for i in child]!=[]:
                    child_write_parent=CreateElement(doc,write_parent,child.tag)
                    searchAllChilds(child,child_write_parent)
                else:
                    object_name_text=child.text
                    if child.tag=="name":
                        object_name_text=classes_changeName[child.text] if child.text in classes_changeName else child.text
                    CreateElement(doc,write_parent,child.tag,object_name_text)
            return xml_objects_num
                    
        doc=xml.dom.minidom.Document()
        
        xml_root=xml_tree.getroot()
        
        root=doc.createElement("annotation")
        doc.appendChild(root)
        root.setAttribute('verified','yes')
        
        
        xml_objects_num=searchAllChilds(xml_root,root)
        
        if xml_objects_num==0:
            sys.exit()
            
        try:
            saveimg_name=xml_root.find("filename").text
            shutil.copy(os.path.join(imagedir_path,saveimg_name),os.path.join(image_SaveDir_path,saveimg_name))
        except BaseException as err:
            print("Error:",err)
        
        with open(os.path.join(NewXML_dir_path,xml_name),"w") as wxml:
            doc.writexml(wxml,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        
        Woutput_CutImage_num+=1    
    except BaseException:
        pass

    
def readXMLandCut(xml_name):
    global Rinput_XML_num,Routput_CutImage_num,output_CutImage_type_num,NotFoundImagetxt_dict
    Rinput_XML_num+=1
    img_num=0
    xml_path=os.path.join(xmldir_path,xml_name)
    try:
        xml_tree=ET.parse(xml_path)
        xml_root=xml_tree.getroot()
        xml_objects=xml_root.findall("object")
        xml_filename=xml_root.find("filename").text
        xml_image_path=os.path.join(imagedir_path,xml_filename)
        
        if not os.path.exists(xml_image_path):
            if os.path.basename(xml_image_path) not in NotFoundImagetxt_dict:
                NotFoundImagetxt_dict[os.path.basename(xml_image_path)]=[]
            NotFoundImagetxt_dict[os.path.basename(xml_image_path)].append(xml_name)
            sys.exit(str(xml_image_path)+" Not Found")
            
        for xml_object in xml_objects:
            xml_class=xml_object.find("name").text
            if xml_class in classes or classes==['']:
                try:
                    if xml_class in classes_changeName:
                        xml_class=classes_changeName[xml_class]
                        
                    if not os.path.exists(os.path.join(cutImage_dir_path,xml_class)):
                        os.mkdir(os.path.join(cutImage_dir_path,xml_class))
                except:
                    pass
                
                xml_object_bndbox=xml_object.find("bndbox")
                img_num+=1
                xmin=int(round(float(xml_object_bndbox.find("xmin").text),0))
                ymin=int(round(float(xml_object_bndbox.find("ymin").text),0))
                xmax=int(round(float(xml_object_bndbox.find("xmax").text),0))
                ymax=int(round(float(xml_object_bndbox.find("ymax").text),0))
                img_name=os.path.splitext(xml_name)[0]+"_"+str(img_num)+imageformat
                CreateCutImage(xmin,ymin,xmax,ymax,img_name,os.path.join(imagedir_path,xml_filename),xml_class,img_num=img_num)
                output_CutImage_type.add(xml_class)
                Routput_CutImage_num+=1
                 
        
    except BaseException as err:
        print("Error:",err)

def ReadXML():
    print("Start create cut Image")
    createdirs()
    T_pool=ThreadPool(processes=threadpool_num)
    for xm in os.listdir(os.path.normpath(xmldir_path))[:1000]:
        if not os.path.splitext(xm)[1]==".xml":
            continue
        T_pool.apply_async(readXMLandCut,args=(xm,))
    T_pool.close()
    T_pool.join()
    if NotFoundImagetxt_dict!={}:
        writeNotFoundImagetxt()
    print("Total input xml number:",Rinput_XML_num)
    print("Total output cutImage number:",Routput_CutImage_num)
    print("Total output cutImage type number:",len(output_CutImage_type))
    print("Create Cut Image Finish!!\n")

def CreateXML():
    print("Start create new xml")
    createdirs()
    T_pool=ThreadPool(processes=threadpool_num)
    for xm in os.listdir(os.path.normpath(xmldir_path)):
        if not os.path.splitext(xm)[1]==".xml":
            continue
        T_pool.apply_async(CreateNewXML,args=(xm,))
    T_pool.close()
    T_pool.join()
    if NotFoundImagetxt_dict!={}:
        writeNotFoundImagetxt()
    print("Total input xml number:",Winput_XML_num)
    print("Total output xml number:",Woutput_CutImage_num)
    print("Create New XML Finish!!\n")
    

def writeNotFoundImagetxt():
    NFTtxt_path=os.path.join(NotFoundImagetxt_path,os.path.splitext(NotFoundImagetxt_name)[0]+str(time.strftime("%Y%m%d", time.localtime()))+".txt")
    if os.path.exists(NFTtxt_path):
        os.remove(NFTtxt_path)
    for k,xs in NotFoundImagetxt_dict.items():
        with open(NFTtxt_path,'a') as NFT:
            NFT.write("未找到的圖片: "+str(k)+"\n")
            NFT.write("未找到圖片的XML: ")
            for x in xs:
                NFT.write(str(x)+",")
            NFT.write("\n\n")
    print("NotFoundImagetxt save path:",NFTtxt_path)

def createdirs():
    try:
        if not os.path.exists(cutImage_dir_path):
            os.makedirs(cutImage_dir_path)
        if not os.path.exists(NewXML_dir_path):
            os.mkdir(NewXML_dir_path)
        if not os.path.exists(image_SaveDir_path):
            os.mkdir(image_SaveDir_path)
    except:
        pass
    
def main():
   if cutFunctionOption in ["Y","y","Yes","yes","YES"]:
        ReadXML()
   if createXMLFunctionOption in ["Y","y","Yes","yes","YES"]:
        CreateXML()
   
if __name__=="__main__":
    try:
        main()
    except BaseException as err:
        print(err)
