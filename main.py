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
            # ✅ Issue #9: Performance Metrics (Before)
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

            # ✅ Issue #9: Performance Metrics (After)
            final_size = len(Cache.Temp_Cache)
            removed = initial_size - final_size
            print(f"Performance Metrics: Processed {initial_size} packets. Cleaned {removed} entries.")
            print(f"Memory Optimization: {final_size} active entries remaining.")

            # ✅ REM Sleep (VIP sorting)
            priority_users = sorted(priority_counter, key=priority_counter.get, reverse=True)[:3]
            print("VIP Users:", priority_users)

        finally:
            print("--- Going back to sleep ---\n")
            Cache_lock.release()

# ... (Thread Start & Main Loop) ...