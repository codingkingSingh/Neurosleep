import socket

HOST = '127.0.0.1'
PORT = 8000

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_socket.connect((HOST, PORT))
    print ("Connected to server at {HOST}:{PORT}")



