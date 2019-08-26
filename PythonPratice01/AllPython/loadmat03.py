import scipy.io as scio
import xml.dom.minidom
import re
from PIL import Image
import hdf5storage
import time
import numpy as np
import re
import os
import shutil


SaveDirPath="D:\\PyAI2\\pedestrian\\PennFudanPed\\XML\\"
SaveDirName="XML"

jpgxmin=0
jpgymin=0


txtdir="D:\\PyAI2\\pedestrian\\PennFudanPed\\Annotation\\"


def getInformation(txtfile):
    with open(txtdir+txtfile,'r') as rinfo:
            imginfo=rinfo.read()
            
            pattern_imginfo_name1=re.compile('''Image\sfilename\s\:\s\"([A-Za-z0-9\/\.]*)\"''')
            imginfo_name1=re.findall(pattern_imginfo_name1,imginfo)[0]
            pattern_imginfo_name2=re.compile('''([A-Za-z0-9]+\.png)''')
            imginfo_name2=re.findall(pattern_imginfo_name2,imginfo_name1)[0]
            
            pattern_imginfo_size=re.compile('''Image size \(X x Y x C\)\ : (\d+)\s*x\s*(\d+)\s*x\s*(\d+)''')
            imginfo_size=re.findall(pattern_imginfo_size,imginfo)[0]
            imginfo_size_width=imginfo_size[0]
            imginfo_size_height=imginfo_size[1]
            imginfo_size_depth=imginfo_size[2]

            pattern_imginfo_label=re.compile('''Original label for object \d* \"[A-Za-z0-9\/\.]*\" \: \"([A-Za-z0-9\/\.]*)\"''')
            imginfo_label=re.findall(pattern_imginfo_label,imginfo)
            
            pattern_imginfo_axis=re.compile('''Bounding box for object \d* "[A-Za-z0-9]*" \(Xmin, Ymin\) - \(Xmax, Ymax\) : \(\s*(\d+)\s*\,\s*(\d+)\s*\)\s*\-\s*\(\s*(\d+)\s*\,\s*(\d+)\s*\)''')
            imginfo_axis=re.findall(pattern_imginfo_axis,imginfo)
            

            return imginfo_name2,imginfo_size,imginfo_label,imginfo_axis

def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element

def CreateXml(jpgName,imgsize,label,axis):
    #im=Image.open(Picturedir+str(jpgName))
    
    doc=xml.dom.minidom.Document()
    root=doc.createElement('annotation')
    doc.appendChild(root)
    root.setAttribute('verified','yes')
    
    folder=doc.createElement('folder')
    folder_name=doc.createTextNode(SaveDirName)
    folder.appendChild(folder_name)
    root.appendChild(folder)

    filename=doc.createElement('filename')
    filename_name=doc.createTextNode(jpgName)
    filename.appendChild(filename_name)
    root.appendChild(filename)

    filepath=doc.createElement('path')
    filepath_path=doc.createTextNode(SaveDirPath+jpgName)
    filepath.appendChild(filepath_path)
    root.appendChild(filepath)

    source=doc.createElement('source')
    root.appendChild(source)
    
    database=doc.createElement('database')
    database_Text=doc.createTextNode("Unknown")
    database.appendChild(database_Text)
    source.appendChild(database)

    size=doc.createElement('size')
    root.appendChild(size)

    width=doc.createElement('width')
    width_Text=doc.createTextNode(str(imgsize[0]))
    width.appendChild(width_Text)
    
    height=doc.createElement('height')
    height_Text=doc.createTextNode(str(imgsize[1]))
    height.appendChild(height_Text)
    
    depth=doc.createElement('depth')
    depth_Text=doc.createTextNode(str(imgsize[2]))
    depth.appendChild(depth_Text)
    
    size.appendChild(width)
    size.appendChild(height)
    size.appendChild(depth)

    segmented=doc.createElement('segmented')
    segmented_Text=doc.createTextNode('0')
    segmented.appendChild(segmented_Text)
    root.appendChild(segmented)

    
    for n,i in enumerate(axis):
        xml_object=doc.createElement('object')
        root.appendChild(xml_object)
        
        Ob_name=CreateElement(doc,xml_object,'name',str(label[n]))
        Ob_pose=CreateElement(doc,xml_object,'pose','Unspecified')
        Ob_truncated=CreateElement(doc,xml_object,'truncated','0')
        Ob_difficult=CreateElement(doc,xml_object,'difficult','0')
        Ob_bndbox=CreateElement(doc,xml_object,'bndbox')
        xmin=int(i[0])
        ymin=int(i[1])
        xmax=int(i[2])
        ymax=int(i[3])
        if xmin>xmax:
            xmax,xmin=xmin,xmax

        if ymin>ymax:
            ymax,ymin=ymin,ymax

        if xmin<jpgxmin:
            xmin=jpgxmin
        
        if ymin<jpgymin:
            ymin=jpgymin
        
        if xmax>=int(imgsize[0]):
            xmax=int(imgsize[0])-1
        
        if ymax>=int(imgsize[1]):
            ymax=int(imgsize[1])-1
            
        Ob_bndbox_xmin=CreateElement(doc,Ob_bndbox,'xmin',str(xmin))
        Ob_bndbox_ymin=CreateElement(doc,Ob_bndbox,'ymin',str(ymin))
        Ob_bndbox_xmax=CreateElement(doc,Ob_bndbox,'xmax',str(xmax))
        Ob_bndbox_ymax=CreateElement(doc,Ob_bndbox,'ymax',str(ymax))

    namepattern=re.compile('''(.*)\.png''')
    xmlname=str(re.findall(namepattern,jpgName)[0])
    
    with open (SaveDirPath+xmlname+".xml","w") as wf:
        doc.writexml(wf,indent='\t', addindent='\t', newl='\n', encoding="utf-8")


def main():
    for txtfile in os.listdir(txtdir):
        CreateXml(*getInformation(txtfile))



if __name__=="__main__":
    main()
