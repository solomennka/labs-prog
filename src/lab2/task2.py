from src.lab2.task1 import wait
import asyncio


async def main():
    """
    Asynchronous function with function calls.
    """
    # Three simultaneous function calls
    await asyncio.gather(
        wait(2, "One"),
        wait(1, "Two"),
        wait(3, "Three"))


if __name__ == "__main__":
    asyncio.run(main())





