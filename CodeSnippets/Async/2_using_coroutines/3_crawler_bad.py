import asyncio

import aiohttp
import platform


async def crawl0(prefix: str, url: str = "") -> None:
    url = url or prefix
    print(f"Crawling {url}...")
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as response:
            text = await response.text()
            for line in text.splitlines():
                if line.startswith(prefix):
                    await crawl0(prefix, line)


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    addr = "https://langa.pl/crawl/"
    asyncio.run(crawl0(addr))
