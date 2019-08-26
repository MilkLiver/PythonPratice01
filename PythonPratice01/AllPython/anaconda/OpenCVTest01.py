# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:21:19 2019

@author: NEIL_YU
"""

import cv2
import numpy as np

image_path=r"D:\test\test2.png"

img=cv2.imread(image_path)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

ret, result_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_OTSU)

print(ret)


img_shape=img.shape
#print(list(img_shape[:2]))
print(img_shape[:2])
img_zero=np.zeros(list(img_shape[:2]))
print(img_zero.shape)
img[...,1]=img_zero

#print(img[:,:,2])
#print(img[...,2].ravel())
print(img[...,2].shape)
#print(img[:,:,2].ravel())    
#print(img[:,:,1].shape)


cv2.imshow("img",img)
cv2.waitKey(0)

#cv2.imshow("img",result_img)
#cv2.waitKey(0)

#ret2,result_img2 = cv2.threshold(gray_img,127,200,cv2.THRESH_BINARY_INV)
#cv2.imshow('img',result_img2)
#cv2.waitKey(0)

cv2.destroyAllWindows()