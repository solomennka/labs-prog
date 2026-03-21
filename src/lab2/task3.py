import time
from typing import Any

import aiohttp as aiohttp
import requests
import asyncio

urls = ["https://www.google.com",
        "https://github.com",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/5"]


def get_url(url: str) -> str and int:
    """
    Function that makes requests to websites without asynchronous programming.
    @param url: str - website link
    @return: str and int - request status and response time
    """
    start = time.perf_counter()
    # Request via the requests library
    res = requests.get(url)
    end = time.perf_counter()
    return res.status_code, end - start


async def fetch(session: Any, url: str):
    """
    Function that makes requests to websites with asynchronous programming.
    @param session: Any - connection manager
    @param url: str - website link
    @return: str - url, status, response time
    """
    start = time.perf_counter()
    # Sending a request
    async with session.get(url) as res:
        # Getting the status
        stat = res.status
        await res.text()
    end = time.perf_counter()
    t = end - start
    print(f"{url} - {stat}, time: {t: .2f} seconds")


def no_async():
    """
    Function for sending requests without asynchronous programming.
    """
    start = time.perf_counter()
    for url in urls:
        stat, t = get_url(url)
        print(f"{url} - {stat}, time: {t: .2f} seconds")
    end = time.perf_counter()
    return end - start


async def with_async():
    """
    Asynchronous function with function calls.
    """
    start = time.perf_counter()
    # Enabling the connection manager
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    print("No async")
    print(f"All time: {no_async(): .2f} seconds\n")
    print("With async")
    print(f"All time: {asyncio.run(with_async()): .2f} seconds")

