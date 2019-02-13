import socket
import sys
import time

##init

s= socket.socket()
host = socket.gethostname()
print("Server will start on host:",host)
port = 8080
s.bind((host,port))
print("")
print("Server done binding to host and port succesfully")
print("")
print("Server is waiting for incoming connections")
s.listen(1)
conn, addr = s.accept()
print(addr,"Connected to the server and online....")
print("")
while 1:
    message = input(str(">> "))
    message= message.encode()
    conn.send(message)
    print("")
    incoming_message=conn.recv(2048)
    incoming_message = incoming_message.decode()
    print("Client: ",incoming_message)
    print("")
    

