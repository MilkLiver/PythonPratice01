import pyautogui
import time
import math
import webbrowser
from selenium import webdriver

chromepath ="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))
a=webbrowser.get('chrome')

i=0
while True:
    if i>=5:
        break
    testurl1="https://translate.google.com.tw/?hl=zh-TW&tab=wT"
    a.open_new(testurl1)
    i+=1

#a.open(testurl1)

#a.open_new_tab(testurl1)
