import asyncio
import time
from typing import Callable, Coroutine

import aiohttp
import platform


async def crawl3(prefix: str, url: str = "") -> None:
    url = url or prefix
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            text = await response.text()
            for line in text.splitlines():
                if line.startswith(prefix):
                    task = asyncio.create_task(
                        crawl3(prefix, line),
                        name=line,
                    )
                    todo.add(task)


async def progress(
        url: str,
        func: Callable[..., Coroutine],
) -> None:
    task = asyncio.create_task(
        func(url),
        name=url,
    )
    todo.add(task)
    start = time.perf_counter()
    while len(todo):
        done, _pending = await asyncio.wait(todo, timeout=0.5)
        todo.difference_update(done)
        urls = (t.get_name() for t in todo)
        print(
            f"tasks in process: {len(todo)}: {', '.join(sorted(urls))[-50:]}"
        )
        await asyncio.sleep(0.5)
    end = time.perf_counter()
    print(f"Took: {int(end-start)} seconds")


async def async_main() -> None:
    try:
        await progress(addr, crawl3)
    except asyncio.CancelledError:
        for task in todo:
            task.cancel()
        done, pending = await asyncio.wait(todo, timeout=1.0)
        todo.difference_update(done)
        todo.difference_update(pending)
        if todo:
            print("warning: new tasks added while cancelling tasks")

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    todo = set()

    addr = "https://langa.pl/crawl/"
    loop = asyncio.get_event_loop()
    task = loop.create_task(async_main())
    loop.call_later(10, task.cancel)
    loop.run_until_complete(task)
