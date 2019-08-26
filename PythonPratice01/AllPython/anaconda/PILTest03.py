# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:54:15 2019

@author: NEIL_YU
"""



from PIL import Image
import skimage
import numpy as np
import matplotlib.pyplot as plt


img=Image.open(r"D:\test\test.png")
img=img.convert("L")


WHITE, BLACK = 255, 0
thresh=skimage.filters.threshold_otsu(np.array(img))
img = img.point(lambda x: WHITE if x > thresh else BLACK)

print(img.size)
#img.save(r"D:\test\test_binary.png")
#img.show()
