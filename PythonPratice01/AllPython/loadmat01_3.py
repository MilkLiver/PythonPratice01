import scipy.io as scio
import xml.dom.minidom
import re
import os
from PIL import Image


SaveDirPath="D:\\PyAI\\CarXml\\"
SaveDirName="CarXML"
NewCarPhotos="D:\\PyAI\\NewCarPhotos\\"

MatName="cars_train_annos"+r".mat"
dataFile=r'D:/PyAI/devkit/'+MatName
imgpath="D:\\PyAI\\cars_train\\"
data=scio.loadmat(dataFile)
info=data['annotations'][0]

#test=data.keys()
#print(list(data))
#print(data['annotations'][0])

jpgxmin=0
jpgymin=0


def CreateElement(doc,parents,name,text=None):
    element=doc.createElement(name)
    if text!=None:
        element_name=doc.createTextNode(text)
        element.appendChild(element_name)
    
    parents.appendChild(element)
    return element


def CreateXml(jpgName,xmin,ymin,xmax,ymax,jpgtype):
    im=Image.open(imgpath+str(jpgName))
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
    filename_name=doc.createTextNode("car_"+str(jpgtype)+"_"+jpgName)
    filename.appendChild(filename_name)
    root.appendChild(filename)

    filepath=doc.createElement('path')
    filepath_path=doc.createTextNode(SaveDirPath+"car_"+str(jpgtype)+"_"+jpgName)
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
    
    im.save(NewCarPhotos+"car_"+str(jpgtype)+"_"+xmlname+'.jpg')
    with open (SaveDirPath+"car_"+str(jpgtype)+"_"+xmlname+".xml","w") as wf:
        doc.writexml(wf,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
    


def main():

    imgfolder = os.path.exists(NewCarPhotos)
    if not imgfolder:
        os.makedirs(NewCarPhotos)
    
    for i in info:
        xmin=i[0][0][0]
        ymin=i[1][0][0]
        xmax=i[2][0][0]
        ymax=i[3][0][0]
        jpgName=i[5][0]
        jpgtype=i[4][0][0]

        
        #print(jpgName,i[4][0])
        #print(info)
        CreateXml(jpgName,xmin,ymin,xmax,ymax,jpgtype)
    print("finish")


main()
