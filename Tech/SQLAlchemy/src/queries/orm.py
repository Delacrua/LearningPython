from sqlalchemy import text, insert, select, func, cast, Integer, and_
from models import WorkersOrm, ResumesOrm

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
    def insert_resumes():
        titles = ["Python Junior Developer", "Python Developer", "Python Data Engineer", "Data Scientist"]
        compensations = [50_000, 150_000, 250_000, 300_000]
        workloads = ["full_time", "full_time", "part_time", "part_time"]
        worker_ids = [1, 1, 2, 2]

        with session_factory() as session:
            session.add_all([
                ResumesOrm(
                    title=titles[i],
                    compensation=compensations[i],
                    workload=workloads[i],
                    worker_id=worker_ids[i],
                ) for i in range(4)
            ])
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

    @staticmethod
    def select_resumes_avg_compensation(language: str, ):
        """
        SELECT workload, AVG(compensation)::int AS avg_compensation
        FROM resumes
        WHERE title LIKE '%Python%' AND compensation > 40000
        GROUP BY workload
        HAVING AVG(compensation)::int > 40000;
        """
        with session_factory() as session:
            query = (
                select(
                    ResumesOrm.workload,
                    cast(func.avg(ResumesOrm.compensation), Integer).label("avg_compensation"),
                )
                .select_from(ResumesOrm)
                .where(and_(
                    ResumesOrm.title.contains(language),
                    ResumesOrm.compensation > 40_000,
                ))
                .group_by(ResumesOrm.workload)
                .having(cast(func.avg(ResumesOrm.compensation), Integer) > 70000)
            )
            print(query.compile(compile_kwargs={"literal_binds": True}))
            result = session.execute(query)
            data = result.all()
            print(f"{data=}")
            print(f"{data[0].avg_compensation}")


async def insert_data_async():
    async with async_session_factory() as session:
        worker_mura = WorkersOrm(username="Async_Muravitskiy")
        worker_pilat = WorkersOrm(username="Async_Pilat")
        session.add_all([worker_mura, worker_pilat])
        await session.commit()

