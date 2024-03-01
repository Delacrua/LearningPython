import asyncio
from typing import Awaitable


async def get_result(awaitable: Awaitable) -> str:
    try:
        result = await awaitable
    except Exception as exc:
        print(f"Exception: {exc}")
        return "No result"
    else:
        return result

def callback(fut: asyncio.Future) -> None:
    print(f"Called by {fut}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #
    # f = asyncio.Future()
    # loop.call_later(5, f.set_result, "this is result")
    # print(loop.run_until_complete(get_result(f)))
    #
    # f = asyncio.Future()
    # loop.call_later(5, f.set_result, "another result")
    # print(loop.run_until_complete(get_result(get_result(get_result(f)))))
    #
    # f = asyncio.Future()
    # loop.call_later(5, f.set_exception, ValueError("oopsiie"))
    # print(loop.run_until_complete(get_result(f)))
    #
    # f = asyncio.Future()
    # loop.call_later(5, f.cancel)
    # print(loop.run_until_complete(get_result(f)))
    #
    # f = asyncio.Future()
    # loop.call_later(5, f.set_result, "final result")
    # print(loop.run_until_complete(
    #     asyncio.gather(
    #         *[get_result(f) for i in range(3)]
    #     )
    # ))

    f = asyncio.Future()
    f.add_done_callback(callback)
    f.add_done_callback(lambda f: loop.stop())
    f.set_result("yeah")
    loop.run_forever()

