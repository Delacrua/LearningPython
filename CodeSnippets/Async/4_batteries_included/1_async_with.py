from dataclasses import dataclass
from typing import Optional

import edgedb


@dataclass
class Connection:
    database_url: str
    connection: Optional[edgedb.AsyncIOConnection] = None

    async def __aenter__(self) -> edgedb.AsyncIOConnection:
        self.connection = await edgedb.async_connect(self.database_url)
        return self.connection

    async def __aexit__(self, type, value, traceback) -> bool:
        if self.connection:
            await self.connection.aclose()
        return False


async def get_users() -> edgedb.Set:
    async with Connection("edgedb://localhost/ambv") as connection:
        result = await connection.query("SELECT USER { name, date_of_birth };")
    return result
