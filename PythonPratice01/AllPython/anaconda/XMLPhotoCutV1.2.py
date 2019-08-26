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
import numpy as np

#參數設定=============================================================
#XML來源資料夾路徑
xmldir_path=r"D:\PyAI\NewOffsetCarXml"
#圖片來源資料夾路徑
imagedir_path=r"D:\PyAI\NewOffsetCarXml"
#裁切後的圖片資料夾路徑
cutImage_dir_path=r"D:\test\cutImages"
#設定圖片的寬高
img_resize_width,img_resize_height=1500,800
#圖檔格式
imageformat=r".png"
#執行緒數量
threadpool_num=3
#XML未找到圖片的錯誤訊息txt檔路徑
NotFoundImagetxt_path=r"D:\test"
#XML未找到圖片的錯誤訊息txt檔名稱
NotFoundImagetxt_name=r"NotFoundImage.txt"
#圖片壓縮率   jpeg:0~100 , png:0~9 , webp:1~100 , PPM,PGM,PBM:0~1
compression_level=0
#===================================================================

input_XML_num=0
output_CutImage_num=0
output_CutImage_type=set()
NotFoundImagetxt_dict={}
image_compression_para=[]
#===================================================================
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

def CreateCutImage(xmin,ymin,xmax,ymax,name,image_path,image_type=None):
    '''img=Image.open(image_path)
    img=img.crop((xmin,ymin,xmax,ymax))
    img=img.resize((img_resize_width,img_resize_height))
    img.save(os.path.join(os.path.join(cutImage_dir_path,image_type),name),quality=quality)'''
    img=cv2.imread(image_path)
    crop_img=img[ymin:ymax,xmin:xmax]
    cv2.imwrite(os.path.join(os.path.join(cutImage_dir_path,image_type),name),crop_img,image_compression_para)

def readXML(xml_name):
    global input_XML_num,output_CutImage_num,output_CutImage_type_num,NotFoundImagetxt_dict
    input_XML_num+=1
    xml_path=os.path.join(xmldir_path,xml_name)
    try:
        xml_tree=ET.parse(xml_path)
        xml_root=xml_tree.getroot()
        xml_objects=xml_root.findall("object")
        xml_image_path=xml_root.find("path")
        source_image_name=os.path.basename(xml_image_path.text)
        if not os.path.exists(xml_image_path.text):
            if os.path.basename(xml_image_path.text) not in NotFoundImagetxt_dict:
                NotFoundImagetxt_dict[os.path.basename(xml_image_path.text)]=[]
            NotFoundImagetxt_dict[os.path.basename(xml_image_path.text)].append(xml_name)
            sys.exit(str(xml_image_path.text)+" Not Found")
        for xml_object in xml_objects:
            if not os.path.exists(os.path.join(cutImage_dir_path,xml_object.find("name").text)):
                os.mkdir(os.path.join(cutImage_dir_path,xml_object.find("name").text))
            xml_object_bndbox=xml_object.find("bndbox")
            xmin=int(xml_object_bndbox[0].text)
            ymin=int(xml_object_bndbox[1].text)
            xmax=int(xml_object_bndbox[2].text)
            ymax=int(xml_object_bndbox[3].text)
            #CreateCutImage(xmin,ymin,xmax,ymax,os.path.splitext(xml_name)[0]+imageformat,xml_image_path.text,xml_object.find("name").text)
            CreateCutImage(xmin,ymin,xmax,ymax,os.path.splitext(xml_name)[0]+imageformat,os.path.join(imagedir_path,source_image_name),xml_object.find("name").text)
            output_CutImage_type.add(xml_object.find("name").text)
            output_CutImage_num+=1
                
        
    except BaseException as err:
        print("Error:",err)

def main():
    print("start")
    createdirs()
    imageCompressionParameterSetting()
    T_pool=ThreadPool(processes=threadpool_num)
    for xm in os.listdir(os.path.normpath(xmldir_path))[:50]:
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
    if not os.path.exists(cutImage_dir_path):
        os.makedirs(cutImage_dir_path)
    
if __name__=="__main__":
    main()
