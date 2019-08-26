# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:54:15 2019

@author: NEIL_YU
"""



from PIL import Image
import skimage
import numpy as np
import matplotlib.pyplot as plt


img=Image.open(r"D:\test\tj01.jpg")
img=img.convert("L")

xmin=1000
ymin=0
xmax=2750
ymax=1600

box=(xmin,ymin,xmax,ymax)


WHITE, BLACK = 255, 0
thresh=skimage.filters.threshold_otsu(np.array(img))-42
img = img.point(lambda x: WHITE if x > thresh else BLACK)

#img2=img.crop((333,161,351,273))
#img2=img.crop(box)
#img2=img2.resize((500,500))

plt.figure()
plt.imshow(img)
plt.show()

print(img.size)
#img2.save(r"D:\test\test2_Overcut.png")
img.save(r"D:\test\tj_binary.png")
#img.show()
