import socket
import datetime as dt
import Cache

Neurosleep_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM )

Port = 8000

LocalHost = '127.0.0.1'

# I chose port 8000, please check this 



Neurosleep_socket.bind((LocalHost, Port))
print("Server is open....")

Neurosleep_socket.listen()

while True: 

    connection, client_address = Neurosleep_socket.accept()

    data = connection.recv(1024) 
    print(data.decode())

    # Storing incoming message into Cache.py
    Cache.Temp_Cache[client_address] = {
        "Message": data.decode(),
        "Timestamp": dt.datetime.now()
    }

    print(Cache.Temp_Cache) # for testing 

    connection.close()
