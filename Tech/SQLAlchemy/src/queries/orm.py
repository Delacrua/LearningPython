from sqlalchemy import text, insert, select
from models import WorkersOrm

from database import sync_engine, async_engine, session_factory, async_session_factory, Base


class SyncORM:

    @staticmethod
    def create_tables():
        sync_engine.echo = True
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_mura = WorkersOrm(username="Muravitskiy")
            worker_pilat = WorkersOrm(username="Pilat")
            session.add_all([worker_mura, worker_pilat])
            session.flush()
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(workers)

    @staticmethod
    def update_worker(worker_id: int, new_username: str):
        with session_factory() as session:
            worker = session.get(WorkersOrm, worker_id)
            worker.username = new_username
            # session.expire_all()
            # session.refresh(worker)
            session.commit()


async def insert_data_async():
    async with async_session_factory() as session:
        worker_mura = WorkersOrm(username="Async_Muravitskiy")
        worker_pilat = WorkersOrm(username="Async_Pilat")
        session.add_all([worker_mura, worker_pilat])
        await session.commit()

