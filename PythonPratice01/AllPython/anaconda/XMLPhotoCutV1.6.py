# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:48:37 2019

@author: NEIL_YU
"""

from multiprocessing.pool import ThreadPool
import xml.etree.ElementTree as ET
#from PIL import Image
import os
import sys
import time
import cv2
import shutil
#import numpy as np

#參數設定=============================================================
#XML來源資料夾路徑
xmldir_path=r"D:\PyAI4\VOCdevkit\VOC2012\Annotations"
#圖片來源資料夾路徑
imagedir_path=r"D:\PyAI4\VOCdevkit\VOC2012\JPEGImages"
#裁切後的圖片資料夾路徑
cutImage_dir_path=r"D:\test\SelectedFileDir\cutImages"
#指定類別挑選出的XML儲存路徑
selectedXML_dir_path=r"D:\test\SelectedFileDir\selectedXML"
#指定類別挑選出的XML進行複製或者移動 c or m 若不想執行任何動作可不填寫參數 selectedXML_behavior=""
selectedXML_behavior="c"
#非指定類別挑選出的XML儲存路徑
NotselectedXML_dir_path=r"D:\test\SelectedFileDir\NotselectedXML"
#非指定類別挑選出的XML進行複製或者移動 c or m 若不想執行任何動作可不填寫參數 selectedXML_behavior=""
NotselectedXML_behavior=""
#圖檔格式
imageformat=r".png"
#執行緒數量
threadpool_num=5
#XML未找到圖片的錯誤訊息txt檔路徑
NotFoundImagetxt_path=r"D:\test\SelectedFileDir"
#XML未找到圖片的錯誤訊息txt檔名稱
NotFoundImagetxt_name=r"NotFoundImage.txt"
#圖片壓縮率   jpeg:0~100 , png:0~9 , webp:1~100 , PPM,PGM,PBM:0~1
compression_level=0
#指定的classes 不指定 classes=""
classes="bus,car,motorbike,person"
#將要進行改名的類別更改名稱  classes_changeName={"要更改的類別名":"更改的類別名稱"} 若不更改:classes_changeName={}
classes_changeName={"motorbike":"moto"}

#===================================================================
classes=classes.split(",")
input_XML_num=0
output_CutImage_num=0
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

def imageCompressionParameterSetting():
    global image_compression_para
    if imageformat==r".jpg":
        image_compression_para=[cv2.IMWRITE_JPEG_QUALITY, compression_level]
    elif imageformat==r".png":
        image_compression_para=[cv2.IMWRITE_PNG_COMPRESSION, compression_level]
    elif imageformat==r".webp":
        image_compression_para=[cv2.IMWRITE_WEBP_QUALITY, compression_level]
    elif imageformat in [r".ppm",r".pbm",r".pgm"]:
        image_compression_para=[cv2.IMWRITE_PXM_BINARY, compression_level]
    else:
        image_compression_para=[]

def CreateCutImage(xmin,ymin,xmax,ymax,name,image_path,image_type=None,img_num=0):
    img=cv2.imread(image_path)
    axisCheck(xmin,ymin,xmax,ymax,(img.shape[0],img.shape[1]))
    crop_img=img[ymin:ymax,xmin:xmax]
    cv2.imwrite(os.path.join(os.path.join(cutImage_dir_path,image_type),name),crop_img,image_compression_para)

def CopyOrMoveXML(xml_path,xml_Savepath,behavior):
    if behavior in ["c","copy","C","COPY","Copy"]:
        shutil.copy(xml_path,xml_Savepath)
                
    if behavior in ["m","move","M","MOVE","Move"]:
        shutil.move(xml_path,xml_Savepath)

def readXML(xml_name):
    global input_XML_num,output_CutImage_num,output_CutImage_type_num,NotFoundImagetxt_dict
    input_XML_num+=1
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
                xmin=int(xml_object_bndbox[0].text)
                ymin=int(xml_object_bndbox[1].text)
                xmax=int(xml_object_bndbox[2].text)
                ymax=int(xml_object_bndbox[3].text)
                img_name=os.path.splitext(xml_name)[0]+"_"+str(img_num)+imageformat
                CreateCutImage(xmin,ymin,xmax,ymax,img_name,os.path.join(imagedir_path,xml_filename),xml_class,img_num=img_num)
                output_CutImage_type.add(xml_class)
                output_CutImage_num+=1
                
        if img_num!=0:
            CopyOrMoveXML(xml_path,os.path.join(selectedXML_dir_path,xml_name),selectedXML_behavior)
        
        elif img_num==0:
            CopyOrMoveXML(xml_path,os.path.join(NotselectedXML_dir_path,xml_name),NotselectedXML_behavior)
                
        
    except BaseException as err:
        print("Error:",err)


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
        if not os.path.exists(selectedXML_dir_path):
            os.makedirs(selectedXML_dir_path)
        if not os.path.exists(NotselectedXML_dir_path):
            os.makedirs(NotselectedXML_dir_path)
    except:
        pass
    
def main():
    print("start")
    createdirs()
    imageCompressionParameterSetting()
    T_pool=ThreadPool(processes=threadpool_num)
    for xm in os.listdir(os.path.normpath(xmldir_path)):
        if not os.path.splitext(xm)[1]==".xml":
            continue
        T_pool.apply_async(readXML,args=(xm,))
    T_pool.close()
    T_pool.join()
    if NotFoundImagetxt_dict!={}:
        writeNotFoundImagetxt()
    print("Total input xml number:",input_XML_num)
    print("Total output cutImage number:",output_CutImage_num)
    print("Total output cutImage type number:",len(output_CutImage_type))
    print("Finish!!")
    
if __name__=="__main__":
    try:
        main()
    except BaseException as err:
        print(err)
