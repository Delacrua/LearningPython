import asyncio
import datetime


def print_curr_time():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_curr_time()
        try:
            await asyncio.sleep(0.50)
        except asyncio.CancelledError:
            print(f"{name} was cancelled")
            break


async def async_main(number_of_runs: int) -> None:
    try:
        await asyncio.wait_for(
            asyncio.gather(
                *[
                    keep_printing(f"Async Main №{i}")
                    for i in range(1, number_of_runs + 1)
                ]
            ),
            5,
        )
    except asyncio.TimeoutError:
        print("Coroutine run got timed out")


if __name__ == "__main__":
    print("Running Async Main 3 times concurrently")
    asyncio.run(async_main(3))
