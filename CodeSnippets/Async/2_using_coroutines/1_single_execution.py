import asyncio
import datetime


def print_curr_time():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_curr_time()
        await asyncio.sleep(0.50)


#  simple async_main implementation
async def async_main() -> None:
    try:
        await asyncio.wait_for(keep_printing("Async Main"), 5)
    except asyncio.TimeoutError:
        print("Coroutine run got timed out")


# More in-depth implementation to show what Awaitable is
async def async_main_in_depth() -> None:
    func = keep_printing("Async Main In-Depth")
    awaitable = asyncio.wait_for(func, 5)
    try:
        await awaitable
    except asyncio.TimeoutError:
        print("Coroutine run got timed out")


if __name__ == "__main__":
    print("Running Async Main")
    asyncio.run(async_main())
    print("Running Async Main in Depth")
    asyncio.run(async_main_in_depth())

