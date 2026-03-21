import asyncio


async def wait(delay: float, message: str):
    """
    Asynchronous function that displays a message after a delay seconds.
    @param delay: float - number of seconds it takes for the message to appear
    @param message: str - displayed message
    """
    await asyncio.sleep(delay)
    print(message)


if __name__ == "__main__":
    asyncio.run(wait(5, "Hello, World!"))
