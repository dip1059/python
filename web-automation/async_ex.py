import asyncio
from datetime import datetime, timedelta

async def async_function_1():
    print("Async function 1")
    print("now: ", datetime.now().timestamp())
    await asyncio.sleep(2)

    print("Async function 1 completed")

async def async_function_2():
    print("Async function 2")
    await asyncio.sleep(1)
    print("Async function 2 completed")

async def main():
    # Run multiple asynchronous functions concurrently
    await asyncio.gather(async_function_1(), async_function_2())

if __name__ == "__main__":
    asyncio.run(main())