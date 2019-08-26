import scipy.io as scio
import xml.dom.minidom
import re
from PIL import Image
import h5py
import hdf5storage
import time
import numpy as np


#SaveDirPath="D:\\PyAI\\CarXml\\"
#SaveDirName="CarXml"

#txtName="content"+r".txt"
#dataFile=r'D:/PyAI2/MSO/'+txtName

#with open("D:/PyAI2/MSO/content.txt",'w') as wtxt:
#    for i in matcontent['imgIdx'][0]:
#        wtxt.write(str(i)+"\n")

#print("="*50)
#print(time.time()-start)
#--------------------------------------------------------------------------



jpgxmin=0
jpgymin=0
jpgxmax=600
jpgymax=400

def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element


def CreateXml(jpgName,xmin,ymin,xmax,ymax):
    im=Image.open('D:\\PyAI\cars_train\\'+str(jpgName))
    #print(im.size[0])
    
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
    width_Text=doc.createTextNode(str(im.size[0]))
    width.appendChild(width_Text)
    
    height=doc.createElement('height')
    height_Text=doc.createTextNode(str(im.size[1]))
    height.appendChild(height_Text)
    
    depth=doc.createElement('depth')
    depth_Text=doc.createTextNode('3')
    depth.appendChild(depth_Text)
    
    size.appendChild(width)
    size.appendChild(height)
    size.appendChild(depth)

    segmented=doc.createElement('segmented')
    segmented_Text=doc.createTextNode('0')
    segmented.appendChild(segmented_Text)
    root.appendChild(segmented)

    xml_object=doc.createElement('object')
    root.appendChild(xml_object)
    Ob_name=CreateElement(doc,xml_object,'name','car')
    Ob_pose=CreateElement(doc,xml_object,'pose','Unspecified')
    Ob_truncated=CreateElement(doc,xml_object,'truncated','0')
    Ob_difficult=CreateElement(doc,xml_object,'difficult','0')
    Ob_bndbox=CreateElement(doc,xml_object,'bndbox')

    if xmin>xmax:
        xmax,xmin=xmin,xmax

    if ymin>ymax:
        ymax,ymin=ymin,ymax

    if xmin<jpgxmin:
        xmin=jpgxmin
        
    if ymin<jpgymin:
        ymin=jpgymin
        
    if xmax>=im.size[0]:
        xmax=im.size[0]-1
        
    if ymax>=im.size[1]:
        ymax=im.size[1]-1
    
        
    Ob_bndbox_xmin=CreateElement(doc,Ob_bndbox,'xmin',str(xmin))
    Ob_bndbox_ymin=CreateElement(doc,Ob_bndbox,'ymin',str(ymin))
    Ob_bndbox_xmax=CreateElement(doc,Ob_bndbox,'xmax',str(xmax))
    Ob_bndbox_ymax=CreateElement(doc,Ob_bndbox,'ymax',str(ymax))

    
    namepattern=re.compile('''\d*''')
    xmlname=re.findall(namepattern,jpgName)[0]
    
    with open (SaveDirPath+xmlname+".xml","w") as wf:
        doc.writexml(wf,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    


def main():
    '''
    xmin=info[3][0][0][0]
    ymin=info[3][1][0][0]
    xmax=info[3][2][0][0]
    ymax=info[3][3][0][0]
    jpgName=info[3][5][0]
    CreateXml(jpgName,xmin,ymin,xmax,ymax)

    print(info[3])'''
    #print(xmin,ymin,xmax,ymax,jpgName)
    #print(info)

'''
    for i in info:
        xmin=i[0][0][0]
        ymin=i[1][0][0]
        xmax=i[2][0][0]
        ymax=i[3][0][0]
        jpgName=i[5][0]
        #print(info)
        CreateXml(jpgName,xmin,ymin,xmax,ymax)'''


main()
