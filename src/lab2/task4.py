import asyncio
import time
import threading


async def print_message(message, delay):
    """"""
    await asyncio.sleep(delay)
    print(message)


def run_print_message(message, delay):
    asyncio.run(print_message(message, delay))


if __name__ == "__main__":
    print("No streams")
    start = time.perf_counter()
    asyncio.run(print_message("One", 2))
    asyncio.run(print_message("Two", 2))
    asyncio.run(print_message("Three", 2))
    end = time.perf_counter()
    t = end - start
    print(f"Time: {t: .2f} seconds\n")

    print("With streams")
    start = time.perf_counter()
    t1 = threading.Thread(target=run_print_message, args=("One", 2))
    t2 = threading.Thread(target=run_print_message, args=("Two", 2))
    t3 = threading.Thread(target=run_print_message, args=("Three", 2))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    end = time.perf_counter()
    t = end - start
    print(f"Time: {t: .2f} seconds\n")
