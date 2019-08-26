from socket import *
import time

address=("127.0.0.1",47487)
client=socket(AF_INET,SOCK_STREAM)
client.connect(address)

while True:
    msg=input("message: ")
    client.send(msg.encode())
    if not msg or msg=="end":
        break
client.close()
