#!/usr/bin/python
# -*- coding: utf-8 -*-
import win32api  
import win32con  
import win32gui
from PIL import Image

def setWallpaper(img):
        bmpImage = Image.open(img)
        newPath = img.replace('.png', '.bmp')
        bmpImage.save(newPath, "BMP")
        img=newPath
        print(img)
        
        regKey = win32api.RegOpenKeyEx(
            win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop",
            0, win32con.KEY_SET_VALUE)
        # 0＝居中 1＝平铺 2＝拉伸
        win32api.RegSetValueEx(regKey, "WallpaperStyle",
                               0, win32con.REG_SZ, "2")
        # 0＝居中 1＝平铺 2＝拉伸
        win32api.RegSetValueEx(regKey, "TileWallpaper",
                               0, win32con.REG_SZ, "0")
        win32api.RegCloseKey(regKey)
        # 设置桌面壁纸并更新
        win32gui.SystemParametersInfo(
            win32con.SPI_SETDESKWALLPAPER, img, win32con.SPIF_SENDWININICHANGE)


if __name__ == "__main__":
    #setWallpaper("C:/Users/NEIL_YU/Pictures/seyana.png")
    setWallpaper("D:/Jayopicture4.png")
    
