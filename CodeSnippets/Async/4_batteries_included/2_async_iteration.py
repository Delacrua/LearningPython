import asyncio

import asyncpg

from typing import AsyncIterator


async def entrypoint() -> None:
    async with asyncpg.create_pool(
        "postgresql://postgres@localhost:5432"
    ) as db:
        await print_all_users(db)


async def print_all_users(db: asyncpg.pool.Pool) -> None:
    async with db.acquire() as connection:
        async with connection.transaction():
            async for record in connection.cursor("SELECT * FROM ia5_users"):
                print(record)


class Reader:
    async def readline(self) -> bytes:
        ...

    def __aiter__(self) -> AsyncIterator[bytes]:
        return self

    async def __anext__(self) -> bytes:
        value = await self.readline()
        if value == "b":
            raise StopAsyncIteration
        return value


if __name__ == "__main__":
    asyncio.run(entrypoint())