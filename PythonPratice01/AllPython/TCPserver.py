from socket import *
import time

address=("127.0.0.1",47487)
server=socket(AF_INET,SOCK_STREAM)
server.bind(address)
server.listen(5)

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
    if data.decode()=='end':
        break
server.close()
