# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:42:52 2019

@author: NEIL_YU
"""

#import moviepy.editor as mp
from PIL import Image
import imageio
import os,sys

imgs_path=r"D:\test\P2MP4Test"
#rimgs_path=r"D:\test\P2MP4Test\resize"

images=[]
print(os.listdir(imgs_path))
for i in os.listdir(imgs_path):
    images.append(Image.open(imgs_path+"\\"+i).resize((700,700)))
    
img=images[0]
#img.save(imgs_path+"\\"+'gif.gif', save_all=True, append_images=images[1:],loop=0,duration=1000,comment=b"aaabb")
#clip = mp.VideoFileClip(imgs_path+"\\"+"gif.gif")
#clip.write_videofile(imgs_path+"\\"+"myvideo.mp4")
#clip.write_videofile(imgs_path+"\\"+"myvideo.avi")


frames = [imageio.imread(imgs_path+"\\"+i) for i in os.listdir(imgs_path)]
#imageio.mimsave(imgs_path+"\\"+"test.gif", frames, 'GIF', duration = 1 / 24)

clips=[imgs_path+"\\"+i for i in os.listdir(imgs_path)]
clip = ImageSequenceClip(clips, fps = 24)
clip.write_videofile('new.mp4')