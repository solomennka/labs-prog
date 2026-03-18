import time

import aiohttp as aiohttp
import requests
import asyncio

urls = ["https://www.google.com",
        "https://github.com",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/5"]


def get_url(url):
    start = time.perf_counter()
    res = requests.get(url)
    end = time.perf_counter()
    return res.status_code, end - start


async def fetch(session, url):
    start = time.perf_counter()
    async with session.get(url) as res:
        stat = res.status
        await res.text()
    end = time.perf_counter()
    t = end - start
    print(f"{url} - {stat}, time: {t: .2f} seconds")


if __name__ == "__main__":
    print("No async")
    start = time.perf_counter()
    for url in urls:
        stat, t = get_url(url)
        print(f"{url} - {stat}, time: {t: .2f} seconds")
    end = time.perf_counter()
    print(f"All time: {end - start: .2f} seconds\n")


async def main():
    print("With async")
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"All time: {end - start: .2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

