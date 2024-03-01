import asyncio
import time
from typing import Callable, Coroutine

import aiohttp
import platform


async def crawl1(prefix: str, url: str = "") -> None:
    url = url or prefix
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            text = await response.text()
            for line in text.splitlines():
                if line.startswith(prefix):
                    todo.add(line)
                    await crawl1(prefix, line)
            todo.discard(url)


async def progress(
        url: str,
        func: Callable[..., Coroutine],
) -> None:
    asyncio.create_task(
        func(url),
        name=url,
    )
    todo.add(url)
    start = time.perf_counter()
    while len(todo):
        print(
            f"tasks in process: {len(todo)}: {', '.join(sorted(todo))[-50:]}"
        )
        await asyncio.sleep(0.5)  # This is actually the gap where created task is active
    end = time.perf_counter()
    print(f"Took: {int(end-start)} seconds")

if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    todo = set()

    addr = "https://langa.pl/crawl/"
    asyncio.run(progress(addr, crawl1))
