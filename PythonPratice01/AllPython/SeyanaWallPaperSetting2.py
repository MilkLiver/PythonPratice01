import urllib.parse
import urllib.request
import re
import win32api  
import win32con  
import win32gui
import time
import win32clipboard

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
    response=urllib.request.urlopen(req)

    with open("D:/Seyana.png","wb") as p:
        p.write(response.read())
        p.close


def GetandSetWallpaper(imgurl):
    getWallpaper(imgurl)
    setWallpaper("D:/Seyana.png")


if __name__=="__main__":
    GetandSetWallpaper("http://p1.music.126.net/Kr5HAy_BD5R0jxA9Xt9UZA==/109951163549389045.jpg")

    
