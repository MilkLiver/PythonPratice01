from socket import *


host=("192.168.8.58",47487)

ser=socket(AF_INET,SOCK_DGRAM)
ser.bind(host)

while True:
    data,addr=ser.recvfrom(2048)
    data=data.decode()
    if not data:
        print("client has exist")
        break
    print("received",data,"from",addr)

ser.close()
