# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:21:48 2019

@author: NEIL_YU
"""

from PIL import Image
from PIL import ImageFilter


img=Image.open(r"D:\test\test.png")
img=img.convert("L")
img=img.convert("1")
img=img.filter(ImageFilter.RankFilter(5,4))

img.show()

