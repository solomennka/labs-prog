import threading
import time

count = 0
lock = threading.Lock()


def increase():
    """
    Function for increasing a global variable.
    """
    global count
    for _ in range(100):
        # Blocking variable increase for only one thread
        with lock:
            c = count
            c += 1
            time.sleep(0.001)
            count = c


if __name__ == "__main__":
    # Creating streams
    threads = [threading.Thread(target=increase) for _ in range(10)]

    # Starting streams
    for t in threads:
        t.start()

    # Waiting for the end of execution of functions in threads
    for t in threads:
        t.join()

    print(f"Wait:", 100*10)
    print(f"Result: {count}")
