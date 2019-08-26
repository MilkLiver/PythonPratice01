# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:54:15 2019

@author: NEIL_YU
"""



from PIL import Image
import skimage
import numpy as np
import matplotlib.pyplot as plt


img=Image.open(r"D:\test\test2.png")
img=img.convert("L")


WHITE, BLACK = 255, 0
thresh=skimage.filters.threshold_otsu(np.array(img))
img = img.point(lambda x: WHITE if x > thresh else BLACK)

img2=img.crop((1000,0,2750,1600))
img2=img2.resize((500,500))

plt.figure()
plt.imshow(img2)
plt.show()

print(img.size)
#img2.save(r"D:\test\test2_cut.png")
#img.show()
