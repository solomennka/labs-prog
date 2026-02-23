import asyncio


async def func1():
    """The first independent function"""
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(4)
    print("Three")


async def func2():
    """The second independent function"""
    print("Four")
    await asyncio.sleep(3)
    print("Five")
    await asyncio.sleep(1)
    print("Six")
    await asyncio.sleep(1)
    print("Seven")


async def main():
    """Running two functions simultaneously"""
    # Creating tasks
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    # Awaiting completion of tasks
    await task1
    await task2
asyncio.run(main())
