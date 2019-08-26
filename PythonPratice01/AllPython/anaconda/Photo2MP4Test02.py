# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:42:52 2019

@author: NEIL_YU
"""

#import moviepy.editor as mp
from PIL import Image
import imageio
import os,sys
from moviepy.editor import *

imgs_path=r"D:\test\P2MP4Test"
rimgs_path=r"D:\test\rphotos"
#rimgs_path=r"D:\test\P2MP4Test\resize"

images=[]
print(os.listdir(imgs_path))
for i in os.listdir(imgs_path):
    im=Image.open(imgs_path+"\\"+i).resize((700,700))
    images.append(im)
    print(i)
    im.save("D:\\test\\rphotos\\"+i)

    
img=images[0]
frames = [imageio.imread(imgs_path+"\\"+i) for i in os.listdir(imgs_path)]
#imageio.mimsave(imgs_path+"\\"+"test.gif", frames, 'GIF', duration = 1 / 24)

print(os.listdir(rimgs_path))
clips=[rimgs_path+"\\"+i for i in os.listdir(rimgs_path)]
print(clips)
clip = ImageSequenceClip(clips, fps = 24)
clip.write_videofile(rimgs_path+"\\"+'new.avi')
