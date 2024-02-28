import asyncio
import sys

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
    pool_size=5,
    max_overflow=10,
)


def get_data_sync():
    with sync_engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        print(f"res= {result.all()}")


async def get_data_async():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT 1,2,3 UNION SELECT 4,5,6"))
        print(f"res= {result.all()}")


if __name__ == "__main__":
    get_data_sync()

    # Only preform check if your code will run on non-windows environments.
    if sys.platform == 'win32':
        # Set the policy to prevent "Event loop is closed" error on Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(get_data_async())
