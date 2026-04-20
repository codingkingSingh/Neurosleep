import socket
import datetime as dt
import Cache
import threading
import time

Cache_lock = threading.Lock()


Neurosleep_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM )

Port = 8000

LocalHost = '127.0.0.1'

# I chose port 8000, please check this 

Neurosleep_socket.bind((LocalHost, Port))
print("Server is open....")

Neurosleep_socket.listen()


def sleeping_thread():
    while True:
        # temporary timer, please change as needed, wakes up every 10 secs
        time.sleep(10) 

        print("Wake up to clean cache")

        Cache_lock.acquire()

        try:
            time_now = dt.datetime.now()

            expired_message= []

            # find expired/old messages, currently setting it up at 30 secs
            for Client, date in Cache.Temp_Cache.items():
                age = (time_now - date["Timestamp"]).seconds
                if age > 30: # please change this as needed
                    expired_message.append(Client)


            for Client in expired_message:
                print(f"{Client} - message deleted")
                del Cache.Temp_Cache[Client]


        finally:
            print ("Going back to sleep")
            Cache_lock.release()   

    

    
cleaner = threading.Thread(target=sleeping_thread)
cleaner.daemon = True
cleaner.start()

while True: 

    connection, client_address = Neurosleep_socket.accept()

    data = connection.recv(1024) 
    print(data.decode())
    Cache_lock.acquire()

    # Storing incoming message into Cache.py
    try:

        Cache.Temp_Cache[client_address] = {
            "Message": data.decode(),
            "Timestamp": dt.datetime.now()
        }

        print(Cache.Temp_Cache) # for testing 
    finally:
        Cache_lock.release()

    connection.close()
    #close connection
    