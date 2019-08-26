from socket import *
import time
import re
import pyautogui

address=("192.168.8.29",47487)
client=socket(AF_INET,SOCK_STREAM)
client.connect(address)

while True:
    try:
        position=client.recv(1024)
        position=position.decode()
        #x=re.search(r"x\d+",position).group()
        #x=int(re.search(r"\d+",x).group())
        #y=re.search(r"y\d+",position).group()
        #y=int(re.search(r"\d+",y).group())
        pattern=re.compile(r'\d+')
        x=int(pattern.findall(position)[0])
        y=int(pattern.findall(position)[1])
        print("X:",x,"Y:",y)
        print(position)
        pyautogui.moveTo(x,y)
    except:
        break

client.close()
