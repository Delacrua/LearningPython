import asyncio
import sys
from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text, String
from config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    pool_size=5,
    max_overflow=10,
)


session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)

str_255 = Annotated[str, 255]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_255: String(255)
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Not showing relationships in repr due to making unexpected loads"""
        cols = [
            f"{col}={getattr(self, col)}"
            for index, col in enumerate(self.__table__.columns.keys())
            if col in self.repr_cols or index < self.repr_cols_num
        ]
        return f"<{self.__class__.__name__} {','.join(cols)}>"

