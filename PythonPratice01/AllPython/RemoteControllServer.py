from socket import *
from multiprocessing import Queue
from threading import Thread
import pyautogui
from pynput import mouse
import time


address=("192.168.8.29",47487)
server=socket(AF_INET,SOCK_STREAM)
server.bind(address)
server.listen(5)

x=0
y=0
mc=0
ms=0
msq=Queue(10)

def MouseControll():
    while True:
        global x,y
        x, y = pyautogui.position()

def MouseClick():
    def click(x, y, button, pressed):
        global mc
        #print(x,y,button,pressed)
        print(str(button)=="Button.right")
        if str(button)=="Button.left" and pressed==True:
            mc="1"
        elif str(button)=="Button.right" and pressed==True:
            mc="2"
        elif str(button)=="Button.middle" and pressed==True:
            mc="3"
        else:
            mc="0"
        

    def scroll(x, y, dx, dy):
        global ms
        #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
        if dy<0:
            ms="-1"
            msq.put(ms)
            #print("down")
        elif dy>0:
            ms="1"
            msq.put(ms)
            #print("up")

    with mouse.Listener(on_click=click,on_scroll=scroll) as listener:
        listener.join()

p =Thread(target=MouseControll, args=())
p2 =Thread(target=MouseClick, args=())
     
p.setDaemon(True)
p2.setDaemon(True)
     
p.start()
p2.start()
while True:
     
     
     #print(position)
     position="x"+str(x)+"y"+str(y)
     print(position)
     print("wait for connect...")
     sta,fro=server.accept()
     print("connect from:",fro)

     while True:
         if not msq.empty():

             ms=msq.get()
         position="x"+str(x)+"y"+str(y)+"ms"+str(ms)+"mc"+str(mc)
         print(position)
         ms="0"
         try:
             #data=sta.recv(1024)
             sta.send(position.encode())
             
             
         except:
             break
     p.join()
     p2.join()

sta.close()
server.close()
