# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:02:38 2019

@author: NEIL_YU
"""

import cv2

img=cv2.imread(r"C:\Users\NEIL_YU\Pictures\www.jpg")
cv2.imwrite(r"C:\Users\NEIL_YU\Pictures\www.png",img,[cv2.IMWRITE_PNG_COMPRESSION,0])