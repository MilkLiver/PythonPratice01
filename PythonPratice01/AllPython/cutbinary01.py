import os
import shutil
import re
import numpy as np
from PIL import Image
import skimage.io
from skimage import data, filters
#import matplotlib.pyplot as plt

loadpath=r"D:\PyAI3\4\cut"
newpath=r"D:\PyAI3\4\binaryImg\img_binary"
imgs_gray_path=r"D:\PyAI3\4\binaryImg\img_gray"

def img_gray(img_loadpath,img_savepath):
    print("g",img_loadpath)
    print("g",img_savepath)
    img=Image.open(img_loadpath)
    img=img.convert("L")
    img.save(img_savepath)
    return img_savepath

def img_binary(img_loadpath,img_savepath):
    print(img_loadpath)
    print(img_savepath)
    img_po = skimage.io.imread(img_loadpath)
    img=Image.open(img_loadpath)
    image = np.array(img)

    WHITE, BLACK = 255, 0
    thresh = filters.threshold_otsu(image)

    img = img.point(lambda x: WHITE if x > thresh else BLACK)
    #img=img.convert('1')

    img_pattern=re.compile("""(.*).jpg""")
    img_savepath=re.findall(img_pattern,img_savepath)[0]
    print(img_savepath+".png")
    
    img.save(img_savepath+".png")

def CopyFile(dirpath,newdirpath,copyfolder=None):
    for i in os.listdir(dirpath):
        if os.path.isdir(dirpath+i):
            CopyFile(dirpath+i+"\\",newdirpath)
        else:
            print(dirpath+i)
            img_binary(img_gray(dirpath+i,imgs_gray_path+"\\"+i),newpath+"\\"+i)
            #shutil.copyfile(dirpath+i,newdirpath+i)
            
def dirclear():
    newdir=os.path.exists(newpath)
    if newdir:        
        shutil.rmtree(newpath)
    os.makedirs(newpath)
        
    imgs_gray_dir=os.path.exists(imgs_gray_path)
    if imgs_gray_dir:
        shutil.rmtree(imgs_gray_path)
    os.makedirs(imgs_gray_path)


def main():
    dirclear()
    CopyFile(loadpath+"\\",newpath+"\\")
    #img_binary(img_gray(r"D:\PyAI3\4\cut\E\SCH_20190109164923_650_plate_1_005.jpg",r"D:\PyAI3\4\binaryImg\test_gray.jpg"),r"D:\PyAI3\4\binaryImg\test_binary.png")


if __name__=="__main__":
    main()


