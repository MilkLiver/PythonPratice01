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


#import tkinter.messagebox as tk

def setWallpaper(img):
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
        try:
            win32gui.SystemParametersInfo(
                win32con.SPI_SETDESKWALLPAPER, img, win32con.SPIF_SENDWININICHANGE)
        except:
            win32api.MessageBox(0, "未抓取到圖片!!", "錯誤",win32con.MB_ICONWARNING)
            print("NO Picture")


def getWallpaper(imgurl):
    url=imgurl

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        "Referer":"https://www.google.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }
    req=urllib.request.Request(url,headers=headers)
    try:
        response=urllib.request.urlopen(req)
    except:
        print("No Get Any Picture!!")
        return
    with open("D:/downloadpicture.png","wb") as p:
        p.write(response.read())
        p.close


def GetandSetWallpaper():
    #getWallpaper(imgurl)
    #setWallpaper("D:/downloadpicture.png")
    time.sleep(0.01)
    setWallpaper("D:/R255.bmp")
    time.sleep(0.01)
    setWallpaper("D:/B255.bmp")


if __name__=="__main__":
        while True:
                GetandSetWallpaper()

    

    
