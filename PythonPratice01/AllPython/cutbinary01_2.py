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
imgformat=r".tif"
fixnum=15

def img_gray(img_loadpath,img_savepath):
    img=Image.open(img_loadpath)
    img=img.convert("L")
    img.save(img_savepath)
    return img_savepath

def img_binary(img_loadpath,img_savepath):
    img_po = skimage.io.imread(img_loadpath)
    img=Image.open(img_loadpath)
    image = np.array(img)

    WHITE, BLACK = 255, 0
    thresh = filters.threshold_otsu(image)+fixnum

    img = img.point(lambda x: WHITE if x > thresh else BLACK)
    #img=img.convert('1')

    img_pattern=re.compile("""(.*).jpg""")
    img_savepath=re.findall(img_pattern,img_savepath)[0]
    #print(img_savepath+".png")
    
    img.save(img_savepath+imgformat)

def CopyFile(dirpath,newdirpath,copyfolder=""):
    for i in os.listdir(dirpath):
        if os.path.isdir(dirpath+i):
            CopyFile(dirpath+i+"\\",newdirpath,copyfolder+i)
        else:
            print(dirpath+i)
            if copyfolder!="":
                
                if not os.path.exists(newpath+"\\"+copyfolder):
                    os.makedirs(newpath+"\\"+copyfolder)
                if not os.path.exists(imgs_gray_path+"\\"+copyfolder):
                    os.makedirs(imgs_gray_path+"\\"+copyfolder)
                    
                img_binary(img_gray(dirpath+i,imgs_gray_path+"\\"+copyfolder+"\\"+i),newpath+"\\"+copyfolder+"\\"+i)
            else:
                img_binary(img_gray(dirpath+i,imgs_gray_path+"\\"+i),newpath+"\\"+i)
                
            
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


if __name__=="__main__":
    main()


