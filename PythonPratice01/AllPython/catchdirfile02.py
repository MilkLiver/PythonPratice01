import numpy as np
import os
import shutil
import re

cutpath="D:\\PyAI3\\4\\cut\\"
parentpath="D:\\PyAI3\\4\\JPEGImages\\"
xmlpath="D:\\PyAI3\\4\\Annotation\\"
NotFoundTxtPath="D:\\PyAI3\\4\\"

newxmlpath="D:\\PyAI3\\4\\selectedXML\\"
newimgpath="D:\\PyAI3\\4\\selectedImg\\"
parentsCount={}
parentsNotFound={}


def CopyFile(dirpath,newdirpath,parpath,cxmlpath,cnewxmlpath):
    parlist=os.listdir(parpath)
    parents=[]
    global parentsCount
    parentImgName_pattern=re.compile("(.*)_plate_")
    global parentsNotFound

    xmllist=os.listdir(cxmlpath)
    xmls=[]
    
    for parent in parlist:
        parentImgName=re.findall(parentImgName_pattern,parent)[0]
        parents.append(parentImgName)

    for cxml in xmllist:
        xmlName=re.findall(parentImgName_pattern,cxml)[0]
        xmls.append(xmlName)
        
        
    for i in os.listdir(dirpath):

        if os.path.isdir(dirpath+i):
            CopyFile(dirpath+i+"\\",newdirpath,parpath,cxmlpath,cnewxmlpath)
        else:
            cutImgName_pattern=re.compile("(.*)_plate_\d*_\d*\.jpg")
            cutImgName=re.findall(cutImgName_pattern,i)[0]
            
            if cutImgName not in parents:
                if cutImgName not in parentsNotFound:
                    parentsNotFound[cutImgName]=[]
                parentsNotFound[cutImgName].append(i)
                continue
            
            if os.path.exists(newdirpath+parlist[parents.index(cutImgName)]):
                parentsCount[parlist[parents.index(cutImgName)]].append(i)
                continue
            #print(cutImgName)
            parentsCount[parlist[parents.index(cutImgName)]]=[]
            parentsCount[parlist[parents.index(cutImgName)]].append(i)            
            shutil.copyfile(parpath+parlist[parents.index(cutImgName)],newdirpath+parlist[parents.index(cutImgName)])
            shutil.copyfile(cxmlpath+xmllist[xmls.index(cutImgName)],cnewxmlpath+xmllist[xmls.index(cutImgName)])

    with open(NotFoundTxtPath+"NotFoundLog.txt","w") as nft:
        for i in parentsCount:
            print("車牌:",i,"找到次數:",len(parentsCount[i]))
            for i in parentsCount[i]:
                print(i)
        print("\n已找到車牌總數:",len(parentsCount))

        print()
    
        for i in parentsNotFound:
            print("未找到車牌:",i,"未找到次數:",len(parentsNotFound[i]))
            nft.write("未找到車牌:"+str(i)+"未找到次數:"+str(len(parentsNotFound[i]))+"\n")
            nft.write("未找到的cut圖:")
            for i in parentsNotFound[i]:
                print(i)
                nft.write(str(i)+",")
            nft.write("\n\n")
        print("\n未找到車牌總數:",len(parentsNotFound),"\n")

    

    
#刪除資料            
def dirclear():
    imgfolder = os.path.exists(newimgpath)
    if imgfolder:
        shutil.rmtree(newimgpath)

    xmlfolder = os.path.exists(newxmlpath)
    if xmlfolder:
        shutil.rmtree(newxmlpath)

    notfoundtxt=os.path.exists(NotFoundTxtPath+"NotFoundLog.txt")
    if notfoundtxt:
        os.remove(NotFoundTxtPath+"NotFoundLog.txt")

    os.makedirs(newimgpath)
    os.makedirs(newxmlpath)

def main():
    dirclear()
    CopyFile(cutpath,newimgpath,parentpath,xmlpath,newxmlpath)

if __name__=="__main__":
    main()



    
