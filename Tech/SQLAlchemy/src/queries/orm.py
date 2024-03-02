from sqlalchemy import insert, select, func, cast, Integer, and_
from sqlalchemy.orm import aliased, joinedload, selectinload, contains_eager
from models import WorkersOrm, ResumesOrm, VacanciesOrm

import schemas as model_dtos

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
    def insert_vacancies_and_replies():
        with session_factory() as session:
            new_vacancy = VacanciesOrm(title="Python Engineer", compensation=100_000)
            resume_1 = session.get(ResumesOrm, 1)
            resume_2 = session.get(ResumesOrm, 2)
            resume_1.vacancies_replied.append(new_vacancy)
            resume_2.vacancies_replied.append(new_vacancy)
            session.commit()



    @staticmethod
    def select_workers():
        with session_factory() as session:
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.scalars().all()
            print(workers)
            workers_dto = [
                model_dtos.WorkersDTO.model_validate(row, from_attributes=True)
                for row in workers
            ]
            print(workers_dto)

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
            data_dto = [
                model_dtos.WorkloadAvgCompensationDTO.model_validate(row, from_attributes=True)
                for row in data
            ]
            print(data_dto)


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
            workers = res.unique().scalars().all()
            print(workers)

            workers_dto = [
                model_dtos.WorkersRelDTO.model_validate(row, from_attributes=True)
                for row in workers
            ]
            print(workers_dto)

    @staticmethod
    def select_workers_with_condition_relationship():
        with session_factory() as session:
            query = (
                select(WorkersOrm)
                .options(selectinload(WorkersOrm.resumes_parttime))
            )

            res = session.execute(query)
            result = res.unique().scalars().all()

            worker_1_resumes = result[0].resumes
            print(worker_1_resumes)

    @staticmethod
    def select_workers_with_condition_relationship_contains_eager():
        with session_factory() as session:
            query = (
                select(WorkersOrm)
                .join(WorkersOrm.resumes)
                .options(contains_eager(WorkersOrm.resumes))
                .filter(ResumesOrm.workload == "part_time")
            )

            res = session.execute(query)
            result = res.unique().scalars().all()

            worker_1_resumes = result[0].resumes
            print(worker_1_resumes)

    @staticmethod
    def select_workers_with_condition_relationship_contains_eager_with_limit():
        with session_factory() as session:
            sub_query = (
                select(ResumesOrm.id.label("parttime_resumes_id"))
                .filter(ResumesOrm.worker_id == WorkersOrm.id)
                .order_by(WorkersOrm.id.desc())
                .limit(2)
                .scalar_subquery()
                .correlate(WorkersOrm)
            )

            query = (
                select(WorkersOrm)
                .join(ResumesOrm, ResumesOrm.id.in_(sub_query))
                .options(contains_eager(WorkersOrm.resumes))
            )

            res = session.execute(query)
            result = res.unique().scalars().all()

            worker_1_resumes = result[0].resumes
            print(worker_1_resumes)

    @staticmethod
    def select_resumes_with_all_relationships():
        with session_factory() as session:
            query = (
                select(ResumesOrm)
                .options(joinedload(ResumesOrm.worker))
                .options(selectinload(ResumesOrm.vacancies_replied).load_only(VacanciesOrm.title))
            )

            res = session.execute(query)
            result_orm = res.unique().scalars().all()
            print(result_orm)

            result_dto = [
                model_dtos.ResumesRelVacanciesRepliedWithoutVacancyCompensationDTO.model_validate(
                    row, from_attributes=True
                ) for row in result_orm]
            print(f"{result_dto=}")
            return result_dto


async def insert_data_async():
    async with async_session_factory() as session:
        worker_mura = WorkersOrm(username="Async_Muravitskiy")
        worker_pilat = WorkersOrm(username="Async_Pilat")
        session.add_all([worker_mura, worker_pilat])
        await session.commit()
