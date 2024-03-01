import asyncio
import datetime

loop = asyncio.get_event_loop()

def print_curr_time():
    print(datetime.datetime.now())


def trampoline(name: str = "") -> None:
    print(f"Trampoline {name}", end=" ")
    print_curr_time()
    loop.call_later(0.5, trampoline, name)

def perform_blocking_operation():
    sum = 0
    for i in range(10_000):
        for j in range(10_000):
            sum += i + j
    return sum


if __name__ == "__main__":
    loop.call_soon(trampoline, "First")
    loop.call_soon(trampoline, "Second")
    loop.call_soon(trampoline, "Third")
    loop.set_debug(True)
    loop.call_later(5, perform_blocking_operation)
    loop.call_later(15, loop.stop)
    loop.run_forever()
