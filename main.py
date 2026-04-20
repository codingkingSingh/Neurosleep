import socket
import datetime as dt
import Cache 
import threading
import time

Cache_lock = threading.Lock()
priority_counter = {} # Fixed: Ensure this is defined at the top

# ... (Socket Setup) ...

def sleeping_thread():
    while True:
        time.sleep(10) 
        print("\n--- Wake up to clean cache ---")
        Cache_lock.acquire()
        try:
            #  Issue #9: Performance Metrics (Before)
            initial_size = len(Cache.Temp_Cache)
            
            time_now = dt.datetime.now()
            expired_message = []

            # Issue #7: Deep Sleep Cleanup
            for Client, data in Cache.Temp_Cache.items():
                age = (time_now - data["Timestamp"]).total_seconds()
                if age > 30:
                    expired_message.append(Client)

            for Client in expired_message:
                print(f"{Client} - message deleted")
                del Cache.Temp_Cache[Client]

            # Issue #9: Performance Metrics (After)
            final_size = len(Cache.Temp_Cache)
            removed = initial_size - final_size
            print(f"Performance Metrics: Processed {initial_size} packets. Cleaned {removed} entries.")
            print(f"Memory Optimization: {final_size} active entries remaining.")

            # REM Sleep (VIP sorting)
            priority_users = sorted(priority_counter, key=priority_counter.get, reverse=True)[:3]
            print("VIP Users:", priority_users)

        finally:
            print("--- Going back to sleep ---\n")
            Cache_lock.release()

Neurosleep_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
LocalHost = '127.0.0.1'
Port = 8000
Neurosleep_socket.bind((LocalHost, Port))
Neurosleep_socket.listen()
print("Server open and listening")

cleaner = threading.Thread(target = sleeping_thread)
cleaner.daemon = True
cleaner.start()

while True:
    connection, client_address = Neurosleep_socket.accept()
    data = connection.recv(1024)

    if data:
        Cache_lock.acquire()
        try:
            ip = client_address
            priority_counter[ip] = priority_counter.get(ip,0)+1

            Cache.Temp_Cache[client_address]= {
                "Message": data.decode(),
                "Timestamp": dt.datetime.now()
            }
        finally: 
            Cache_lock.release()

        connection.close()