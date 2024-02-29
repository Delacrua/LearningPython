from sqlalchemy import insert, select, func, cast, Integer, and_
from sqlalchemy.orm import aliased, joinedload, selectinload
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
    def insert_additional_resumes():
        with session_factory() as session:
            workers = [
                {"username": "Artem"},
                {"username": "Roman"},
                {"username": "Petr"},
            ]
            resumes = [
                {"title": "Python программист", "compensation": 60000, "workload": "full_time", "worker_id": 3},
                {"title": "Machine Learning Engineer", "compensation": 70000, "workload": "part_time", "worker_id": 3},
                {"title": "Python Data Scientist", "compensation": 80000, "workload": "part_time", "worker_id": 4},
                {"title": "Python Analyst", "compensation": 90000, "workload": "full_time", "worker_id": 4},
                {"title": "Python Junior Developer", "compensation": 100000, "workload": "full_time", "worker_id": 5},
            ]
            insert_workers = insert(WorkersOrm).values(workers)
            insert_resumes = insert(ResumesOrm).values(resumes)
            session.execute(insert_workers)
            session.execute(insert_resumes)
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

    @staticmethod
    def select_with_join_cte_subquery_window_func():
        """
        WITH helper2 AS (
        SELECT *, compensation-avg_workload_compensation AS compensation_diff
        FROM
        (SELECT
        w.id,
        w.username,
        r.compensation,
        r.workload,
        AVG(r.compensation) OVER (PARTITION BY workload)::int AS avg_workload_compensation
        FROM resumes r
        JOIN workers w ON r.worker_id = w.id) helper1
        )
        SELECT * FROM helper2
        ORDER BY compensation_diff DESC
        """
        with session_factory() as session:
            r = aliased(ResumesOrm)
            w = aliased(WorkersOrm)
            subquery = (
                select(
                    r,
                    w,
                    func.avg(r.compensation).over(partition_by=r.workload).cast(Integer).label("avg_workload_compensation")
                )
                .join(r, r.worker_id == w.id).subquery("helper1")
            )
            cte = (
                select(
                    subquery.c.id,
                    subquery.c.username,
                    subquery.c.compensation,
                    subquery.c.workload,
                    subquery.c.avg_workload_compensation,
                    (subquery.c.compensation - subquery.c.avg_workload_compensation).label("compensation_diff")
                )
                .cte("helper2")
            )
            query = (
                select(cte)
                .order_by(cte.c.compensation_diff.desc())
            )
            print(query.compile(compile_kwargs={"literal_binds": True}))

            res = session.execute(query)
            result = res.all()
            print(result)

    @staticmethod
    def select_workers_with_lazy_relationship():
        with session_factory() as session:
            query = (
                select(WorkersOrm)
            )

            res = session.execute(query)
            result = res.scalars().all()

            worker_1_resumes = result[0].resumes
            print(worker_1_resumes)

            worker_2_resumes = result[1].resumes
            print(worker_2_resumes)

    @staticmethod
    def select_workers_with_joined_relationship():
        with session_factory() as session:
            query = (
                select(WorkersOrm)
                .options(joinedload(WorkersOrm.resumes))
            )

            res = session.execute(query)
            result = res.unique().scalars().all()

            worker_1_resumes = result[0].resumes
            print(worker_1_resumes)

            worker_2_resumes = result[1].resumes
            print(worker_2_resumes)

    @staticmethod
    def select_workers_with_selectin_relationship():
        with session_factory() as session:
            query = (
                select(WorkersOrm)
                .options(selectinload(WorkersOrm.resumes))
            )

            res = session.execute(query)
            result = res.unique().scalars().all()

            worker_1_resumes = result[0].resumes
            print(worker_1_resumes)

            worker_2_resumes = result[1].resumes
            print(worker_2_resumes)


async def insert_data_async():
    async with async_session_factory() as session:
        worker_mura = WorkersOrm(username="Async_Muravitskiy")
        worker_pilat = WorkersOrm(username="Async_Pilat")
        session.add_all([worker_mura, worker_pilat])
        await session.commit()
