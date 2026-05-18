import asyncio
import time
import threading


async def print_message(message: str, delay: float):
    """
    Asynchronous function that displays a message after a delay seconds.
    @param delay: float - number of seconds it takes for the message to appear
    @param message: str - displayed message
    """
    await asyncio.sleep(delay)
    print(message)


def run_print_message(message: str, delay: int):
    """
    Launches the print_message function.
    @param delay: float - number of seconds it takes for the message to appear
    @param message: str - displayed message
    """
    asyncio.run(print_message(message, delay))


def no_stream():
    """
    Function for three print_message function calls
    """
    # Calling an asynchronous function
    start = time.perf_counter()
    asyncio.run(print_message("One", 2))
    asyncio.run(print_message("Two", 2))
    asyncio.run(print_message("Three", 2))
    end = time.perf_counter()
    t = end - start
    return t


def streams():
    """
    function for creating three threads and calling a function in them.
    """
    # Creating streams
    start = time.perf_counter()
    threads = [threading.Thread(target=run_print_message, args=("One", 2)),
                threading.Thread(target=run_print_message, args=("Two", 2)),
                threading.Thread(target=run_print_message, args=("Three", 2))]

    # Starting streams
    for t in threads:
        t.start()

    # Waiting for the end of execution of functions in threads
    for t in threads:
        t.join()

    end = time.perf_counter()
    t = end - start
    return t


if __name__ == "__main__":
    print("No streams")
    t1 = no_stream()
    print(f"Time: {t1: .2f} seconds\n")
    print("With streams")
    t2 = streams()
    print(f"Time: {t2: .2f} seconds\n")
