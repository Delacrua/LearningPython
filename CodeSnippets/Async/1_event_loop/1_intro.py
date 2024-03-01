import asyncio
import datetime

loop = asyncio.get_event_loop()

def print_curr_time():
    print(datetime.datetime.now())


if __name__ == "__main__":
    loop.call_soon(print_curr_time)
    loop.call_soon(print_curr_time)

    loop.run_until_complete(asyncio.sleep(5))