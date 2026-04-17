import socket 

Neurosleep_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM )

Port = 8000

# I chose port 8000, please check this 


Neurosleep_socket.bind('', Port)
print("Server is open....")