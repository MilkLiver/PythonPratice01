import scipy.io as scio
import xml.dom.minidom
import re
from PIL import Image
import hdf5storage
import time
import numpy as np
import re
import os


SaveDirPath="D:\\test\\tXML\\"
SaveDirName="tXML"
Picturedir="D:\\PyAI2\\MSO\\img\\"
NewPhotos="D:\\test\\tNewPhoto\\"

jpgxmin=0
jpgymin=0

matName="imgIdx"+r".mat"
matdataFile=r'D:/PyAI2/MSO/'+matName

#是否產生txt檔 True or False
createtxt=False
txtName="test"+r".txt"
dataFile=r'D:/PyAI2/MSO/'+txtName

def MatToTxt():
    start=time.time()
    matcontent = hdf5storage.loadmat(matdataFile)
    with open(dataFile,'w') as wtxt:
        for i in matcontent['imgIdx'][0]:
            wtxt.write(str(i)+"\n")
    print(time.time()-start)

def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element

def CreateXml(jpgName,axis,imglabel):
    im=Image.open(Picturedir+str(jpgName))
    
    doc=xml.dom.minidom.Document()
    root=doc.createElement('annotation')
    doc.appendChild(root)
    root.setAttribute('verified','yes')
    
    folder=doc.createElement('folder')
    folder_name=doc.createTextNode(SaveDirName)
    folder.appendChild(folder_name)
    root.appendChild(folder)

    filename=doc.createElement('filename')
    filename_name=doc.createTextNode(imglabel+"_"+jpgName)
    filename.appendChild(filename_name)
    root.appendChild(filename)

    filepath=doc.createElement('path')
    filepath_path=doc.createTextNode(SaveDirPath+imglabel+"_"+jpgName)
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

    
    for i in axis:
        xml_object=doc.createElement('object')
        root.appendChild(xml_object)
        Ob_name=CreateElement(doc,xml_object,'name','object')
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
        
        if xmax>=im.size[0]:
            xmax=im.size[0]-1
        
        if ymax>=im.size[1]:
            ymax=im.size[1]-1
        Ob_bndbox_xmin=CreateElement(doc,Ob_bndbox,'xmin',str(xmin))
        Ob_bndbox_ymin=CreateElement(doc,Ob_bndbox,'ymin',str(ymin))
        Ob_bndbox_xmax=CreateElement(doc,Ob_bndbox,'xmax',str(xmax))
        Ob_bndbox_ymax=CreateElement(doc,Ob_bndbox,'ymax',str(ymax))

    
    namepattern=re.compile('''(.*)\.jpg''')
    xmlname=str(re.findall(namepattern,jpgName)[0])

    im.save(NewPhotos+str(imglabel)+"_"+xmlname+'.jpg')
    
    with open (SaveDirPath+str(imglabel)+"_"+xmlname+".xml","w") as wf:
        doc.writexml(wf,indent='\t', addindent='\t', newl='\n', encoding="utf-8")

def ReadTxtAndCreateXml():
    imgfolder = os.path.exists(NewPhotos)
    if not imgfolder:
        os.makedirs(NewPhotos)
        
    with open(dataFile,'r') as cf:
        pattern=re.compile('\'([\S]+\.jpg).*\[\[(\d+).*array\(([\W\d]*)')
        result=re.findall(pattern,cf.read())
        for i in result:
            imglabel=i[1]
            pattern_axis=re.compile('\d+')
            result_axis=re.findall(pattern_axis,i[2])
            axis=np.array([])
            for i2 in result_axis:
                axis=np.append(axis,int(i2))
            if np.size(axis)!=0:
                axis=axis.reshape(-1,4)
            #print(i[0],axis)
            CreateXml(i[0],axis,imglabel)

def main():
    if createtxt:
        MatToTxt()
    ReadTxtAndCreateXml()



if __name__=="__main__":
    main()
