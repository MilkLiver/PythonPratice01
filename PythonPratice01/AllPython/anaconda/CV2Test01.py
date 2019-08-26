# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:02:40 2019

@author: NEIL_YU
"""

from PIL import Image
import cv2
import matplotlib.pyplot as mp

img=Image.open(r"D:\test\test2.png")
cimg=cv2.imread(r"D:\test\ctest2.png")


try:
    #img.save(r"D:\test\openCVTestPhoto\Comtest2.png",quality=8)
    '''cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.png",cimg,[cv2.IMWRITE_PNG_COMPRESSION, 9])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.jpg",cimg,[cv2.IMWRITE_JPEG_QUALITY, 50])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.webp",cimg,[cv2.IMWRITE_WEBP_QUALITY, 50])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.ppm",cimg,[cv2.IMWRITE_PXM_BINARY, 1])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.pgm",cimg,[cv2.IMWRITE_PXM_BINARY, 1])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.pbm",cimg,[cv2.IMWRITE_PXM_BINARY, 1])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.bmp",cimg,[])
    cv2.imwrite(r"D:\test\openCVTestPhoto\Comctest2.tiff",cimg,[])'''
    #1000,0,2750,1600
    print(cimg.shape)
    crop_cimg=cimg[0:1600,1000:2750]
    print(crop_cimg.shape)
    mp.figure()
    mp.imshow(crop_cimg)
    mp.show()
    cv2.imwrite(r"D:\test\openCVTestPhoto\cut_Comctest2.png",crop_cimg,[])
except BaseException as err:
    print(err)