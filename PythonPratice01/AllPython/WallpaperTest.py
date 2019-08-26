import urllib.parse
import urllib.request
import re
import win32api  
import win32con  
import win32gui
import time
import win32clipboard
import win32con
import time
import random
import numpy as np
from PIL import Image
#import tkinter.messagebox as tk

#圖片網址列表
imgurl=["https://i.imgur.com/shiOfDe.jpg",
        "https://i.imgur.com/aU045Nn.png",
        "https://i.imgur.com/O0UyvTj.png",
        "https://i.imgur.com/VocOJIX.png",
        "https://i.imgur.com/x2PtZsv.png",
        "https://i.imgur.com/aIh4ABS.png",
        "https://i.imgur.com/u2kxHhr.png",
        ]

#DownloadWallpaper=[]
DownloadWallpaper=np.array([])

#倫循時間
ChangeTime=5




#設定桌布
def setWallpaper(img):
        regKey = win32api.RegOpenKeyEx(
            win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop",
            0, win32con.KEY_SET_VALUE)
        
        # 0＝居中 1＝平铺 2＝延伸
        win32api.RegSetValueEx(regKey, "WallpaperStyle",
                               0, win32con.REG_SZ, "2")

        win32api.RegCloseKey(regKey)

        try:
            win32gui.SystemParametersInfo(
                win32con.SPI_SETDESKWALLPAPER, img, win32con.SPIF_SENDWININICHANGE)
        except:
            getWallpaper()
            #win32api.MessageBox(0, "未抓取到圖片!!", "錯誤",win32con.MB_ICONWARNING)
            

#抓取圖片
def getWallpaper():
        
    global DownloadWallpaper
    DownloadWallpaper=[]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }

    for i in range(len(imgurl)):
        url=imgurl[i]
    
        req=urllib.request.Request(url,headers=headers)
        try:
            response=urllib.request.urlopen(req)
        except:
            print("No Get Any Picture!!")
            return
        
        JayoWallpaper="D:/Jayopicture"+str(i)+".png"
        
        #DownloadWallpaper.append(JayoWallpaper)
        
        with open(JayoWallpaper,"wb") as p:
            p.write(response.read())
            p.close
            
        bmpImage = Image.open(JayoWallpaper)
        newPath = JayoWallpaper.replace('.png', '.bmp')
        bmpImage.save(newPath, "BMP")
        DownloadWallpaper.append(newPath)

#抓取及設定圖片
def GetandSetWallpaper():
    getWallpaper()
    while True:
        random.shuffle(DownloadWallpaper)
        for i in DownloadWallpaper:
            print(i)
            #setWallpaper("D:/downloadpicture"+str(i)+".jpg")
            #setWallpaper(i)
            time.sleep(ChangeTime)

#主程式
if __name__=="__main__":
    try:
        while True:
            GetandSetWallpaper()
            #time.sleep(1800)
    except:
        win32api.MessageBox(0, "發生錯誤!!", "錯誤",win32con.MB_ICONWARNING)
        print("copy error!!")

    

    
