# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:08:40 2019

@author: NEIL_YU
"""

import xml.dom.minidom
import xml.etree.ElementTree as ET
import os
import re

xmldir=r"D:\PyAI4\VOCdevkit\VOC2012\txm"
savedir=r"D:\test\tWXML"

pattern=re.compile("\w+")

def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element

def CreateXML(xml_name):
    xml_tree=ET.parse(os.path.join(xmldir,xml_name))
    def searchAllChilds(read_parent,write_parent):
        nonlocal doc
        for child in read_parent:
            if [i for i in child]!=[]:
                child_write_parent=CreateElement(doc,write_parent,child.tag)
                searchAllChilds(child,child_write_parent)
            else:
                CreateElement(doc,write_parent,child.tag,child.text)
                
    doc=xml.dom.minidom.Document()
    
    xml_root=xml_tree.getroot()
    
    root=doc.createElement("annotation")
    doc.appendChild(root)
    root.setAttribute('verified','yes')
    
    searchAllChilds(xml_root,root)
    
    with open(os.path.join(savedir,xml_name),"w") as wxml:
        doc.writexml(wxml,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    
    
def main():
    for i in os.listdir(xmldir):
        if i.endswith(".xml"):
            
            CreateXML(i)

if __name__=="__main__":
    main()