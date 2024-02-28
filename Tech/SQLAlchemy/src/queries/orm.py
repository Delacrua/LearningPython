from sqlalchemy import text, insert
from models import metadata_obj, WorkersOrm

from database import sync_engine, async_engine, session_factory, async_session_factory


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
    with session_factory() as session:
        worker_mura = WorkersOrm(username="Muravitskiy")
        worker_pilat = WorkersOrm(username="Pilat")
        session.add_all([worker_mura, worker_pilat])
        session.commit()


async def insert_data_async():
    async with async_session_factory() as session:
        worker_mura = WorkersOrm(username="Async_Muravitskiy")
        worker_pilat = WorkersOrm(username="Async_Pilat")
        session.add_all([worker_mura, worker_pilat])
        await session.commit()

