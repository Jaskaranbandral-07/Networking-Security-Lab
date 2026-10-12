import time

sent_time = time.time()
current_time = time.time()

if current_time - sent_time <= 5:
    print("Timestamp: VALID")
else:
    print("Timestamp: EXPIRED")
