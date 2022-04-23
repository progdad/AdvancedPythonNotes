import asyncio
import time


# Coroutines are a more generalized form of subroutines(usual functions or procedures).
# Subroutines are entered at one point and exited at another point.
# Coroutines can be entered, exited, and resumed at many different points.

# Coroutine function is a unction which returns a coroutine object.
# A coroutine function may be defined with the async def statement,
# and may contain await, async for, and async with keywords.


# TO ACTUALLY RUN A COROUTINE, ASYNCIO PROVIDES THREE MAIN MECHANISMS:

# 1. The asyncio.run() function to run the top-level entry point “main()” function;
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())


###


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


# 2. Awaiting on a coroutine
async def awaitable():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(awaitable())


# 3. The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.
async def tasks():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(tasks())
