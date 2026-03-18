import threading
import time

count = 0
lock = threading.Lock()


def increase():
    global count
    for _ in range(100):
        with lock:
            c = count
            c += 1
            time.sleep(0.001)
            count = c


threads = [threading.Thread(target=increase) for _ in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Wait:", 100*10)
print(f"Result: {count}")
