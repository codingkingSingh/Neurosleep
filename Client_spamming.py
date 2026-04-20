import socket

LocalHost = '127.0.0.1'
Port = 8000
burst_amount = 5000

print("===== Stress Test Begin =====")
print("Starting spam burst: Sending " + str(burst_amount) + " packets...")
print("Target: Neurosleep_socket on Port " + str(Port))

for i in range(burst_amount):
    try:
        Client_Spam_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Client_Spam_socket.connect((LocalHost, Port))

        message = "Spam Packet #" + str(i)
        Client_Spam_socket.sendall(message.encode())

        Client_Spam_socket.close()

        # Check status of burst attack
        if i % 500 == 0:
            print("Status: " + str(i) + " packets sent...")
    except:
        print("Connection refused: The server's request queue is overwhelmed!")
        break

print("Burst finished. Total packets sent: " + str(i + 1))