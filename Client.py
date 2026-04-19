import socket
 
LocalHost = '127.0.0.1' 
Port = 8000         
 
Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect((LocalHost, Port))

message = "Test Message"

Client_socket.sendall(message.encode())

print(message)

Client_socket.close()
