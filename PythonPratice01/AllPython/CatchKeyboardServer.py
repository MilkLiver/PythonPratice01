from pynput.keyboard import Listener
from pynput import mouse
from socket import *


address=("192.168.8.108",47487)
server=socket(AF_INET,SOCK_STREAM)
server.bind(address)
server.listen(5)


if __name__=="__main__":
    while True:
        print("wait for connect...")
        sta,fro=server.accept()
        print("connect from:",fro)
    
        while True:
            data=sta.recv(1024)
            if not data.decode() or data.decode()=='end':
                break
            print("receive message:",data.decode())
        sta.close()
    server.close()
