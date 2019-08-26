# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:42:52 2019

@author: NEIL_YU
"""

import moviepy.editor as mp
from PIL import Image
import os,sys

#初始圖片位置
imgs_path=r"D:\test\ppp"
#調整後圖片位置
rimgs_path=r"D:\test\rphotos"
#gif儲存位置
gif_path=r"D:\test"
#gif名稱
gif_name=r"gif.gif"
#mp4儲存位置
movie_path=r"D:\test"
#mp4名稱
movie_name=r"myvideo.mp4"
#設定圖片的寬高
img_resize_width,img_resize_height=1600,800
#每張圖間格時間
durationtime=500
#gif播放次數
looptimes=1

images=[]
for i in os.listdir(imgs_path):
    im=Image.open(os.path.join(imgs_path,i)).resize((img_resize_width,img_resize_height))
    images.append(im)
    im.save(os.path.join(rimgs_path,i))
    
img=images[0]
img.save(os.path.join(gif_path,gif_name), save_all=True, append_images=images[1:],loop=looptimes-1,duration=durationtime)
#img.save(os.path.join(gif_path,'gif.gif'), save_all=True, append_images=images[1:],loop=0,duration=1000,comment=b"aaabb")
clip = mp.VideoFileClip(os.path.join(gif_path,gif_name))
clip.write_videofile(os.path.join(movie_path,movie_name))

