# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:42:52 2019

@author: NEIL_YU
"""

#import moviepy.editor as mp
from PIL import Image
import imageio
import os

#初始圖片位置
imgs_path=r"D:\test\ppp"
#調整後圖片位置
rimgs_path=r"D:\test\rphotos"
#mp4儲存位置
movie_path=r"D:\test"
#mp4名稱
movie_name=r"myvideo.mp4"
#設定圖片的寬高
img_resize_width,img_resize_height=1600,800

images=[]
for i in os.listdir(imgs_path):
    im=Image.open(os.path.join(imgs_path,i)).resize((img_resize_width,img_resize_height))
    images.append(im)
    im.save(os.path.join(rimgs_path,i))

    
img=images[0]
#kargs = { 'duration': 1 }
frames = [imageio.imread(os.path.join(rimgs_path,i)) for i in os.listdir(rimgs_path)]
#imageio.mimsave(os.path.join(movie_path,"test.gif"), frames, format='gif',**kargs)
imageio.mimsave(os.path.join(movie_path,movie_name), frames, format='mp4')
