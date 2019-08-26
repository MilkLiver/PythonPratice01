# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:44:30 2019

@author: NEIL_YU
"""
from multiprocessing.pool import ThreadPool
import threading 
import xml.dom.minidom
import xml.etree.ElementTree as ET
from PIL import Image
import re
import platform
import os
import sys

testXML=r"D:\PyAI\CarXml\1_00163.xml"
xmldir_path=r"D:\PyAI\CarXml"
new_xmldir_path=r"D:\PyAI\OffsetCarXml"

x_offset=0
y_offset=0
RthreadNum=1

plat_sys=platform.system()
#xml_dexml=re.compile("(.*).xml")
#xml_rname=re.compile("([-_]{1}[rR]{1})(\d+)")
#txt_pattern=re.compile("(.*).txt")

def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element


def XML_Offset(xml_name="xml_name",img_name=r"name",x_offset=0,y_offset=0):
    doc=xml.dom.minidom.Document()
    root=doc.createElement('annotation')
    doc.appendChild(root)
    root.setAttribute('verified','yes')
    
    tree=ET.parse(testXML)
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
        os.exit()
        
    img=Image.open(img_path)
    
    img_width,img_height=img.size[0],img.size[1]
    print(img_width,img_height)
    
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
        xmin,ymin,xmax,ymax=[int(xml_axis.text) for xml_axis in objs[4]]
        #print(xmin,ymin,xmax,ymax)
        if xmin-x_offset<=0:
            print("test1")
            os.exit()
        if ymin-y_offset<=0:
            print("test2")
            os.exit()
        if xmax+x_offset>=img_width:
            print("test3")
            os.exit()
        if ymax+y_offset>=img_height:
            print("test4")
            os.exit()
        
        
        CreateElement(doc,obj,"xmin",str(xmin))
        CreateElement(doc,obj,"ymin",str(ymin))
        CreateElement(doc,obj,"xmax",str(xmax))
        CreateElement(doc,obj,"ymax",str(ymax))
        
    with open(new_xmldir_path+"\\"+xml_name+".xml","wb") as wxml:
        doc.writexml(wxml,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    print("OwO")

def SaveDirCreate():
    if not os.path.exists(new_xmldir_path):
        os.mkdir(new_xmldir_path)

def main():
    SaveDirCreate()
    pool=ThreadPool(processes=RthreadNum)
    pool.apply_async(XML_Offset,args=("name",x_offset,y_offset))
    #pool.apply_async(XML_Offset,args=("name",x_offset,y_offset))
    pool.close()
    pool.join()
    #getXML_info(offset=offset)
    print("finish")


if __name__=="__main__":
    main()



