import asyncio


async def wait(delay, message):
    """"""
    await asyncio.sleep(delay)
    print(message)


if __name__ == "__main__":
    asyncio.run(wait(5, "Hello, World!"))
