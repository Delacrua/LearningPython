from sqlalchemy import text, insert, select, update
from models import metadata_obj, workers_table

from database import sync_engine, async_engine


def get_data_sync():
    with sync_engine.connect() as conn:
        result = conn.execute(text("SELECT VERSION()"))
        print(f"res= {result.all()}")


async def get_data_async():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT 1,2,3 UNION SELECT 4,5,6"))
        print(f"res= {result.all()}")


class SyncCore:

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_data():
        with sync_engine.connect() as conn:
            # stmt = text(
            #     """
            #     INSERT INTO workers (username) VALUES
            #     ('Muravitsky'),
            #     ('Pilat');
            #     """
            # )
            stmt = insert(workers_table).values(
                [
                    {"username": "Muravitsky"},
                    {"username": "Pilat"},
                ]
            )
            conn.execute(stmt)
            conn.commit()

    @staticmethod
    def select_workers():
        with sync_engine.connect() as conn:
            query = select(workers_table)
            result = conn.execute(query)
            workers = result.all()
            print(workers)

    @staticmethod
    def update_worker(worker_id: int, new_username: str):
        with sync_engine.connect() as conn:
            # stmt = text("UPDATE workers SET username=:username WHERE id=:id")
            # stmt = stmt.bindparams(username=new_username, id=worker_id)
            stmt = (
                update(workers_table).values(
                    username=new_username
                # ).where(workers_table.c.id == worker_id)
                ).filter_by(id=worker_id)
            )

            conn.execute(stmt)
            conn.commit()
