from socket import *

address=("192.168.8.58",47487)
client=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('message: ')
    msg=msg.encode()
    client.sendto(msg.encode(),address)
    if not msg:
        break

client.close()
