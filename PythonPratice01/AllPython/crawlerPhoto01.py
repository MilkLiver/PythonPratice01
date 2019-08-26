import urllib.parse
import urllib.request
import re


url="http://p1.music.126.net/Kr5HAy_BD5R0jxA9Xt9UZA==/109951163549389045.jpg"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Referer":"https://www.google.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
req=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(req)

with open("D:/testSeyana.png","wb") as p:
    p.write(response.read())
    p.close
