import pyautogui
import time
import math
import webbrowser
from selenium import webdriver

OUO=pyautogui.size()
width, height = pyautogui.size()

time.sleep(2)
pyautogui.typewrite('Hello world!', 0.01)
pyautogui.typewrite(['enter'], 0.1)
pyautogui.typewrite('Hello world!', 0.01)
