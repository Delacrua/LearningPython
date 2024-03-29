import datetime
from typing import Optional, Annotated, List

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text, CheckConstraint, Index, \
    PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_255
import enum


metadata_obj = MetaData()


int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now() + interval '1 min')")
)]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow
    )]


class Workload(enum.Enum):
    part_time = "part_time"
    full_time = "full_time"


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int_pk]
    username: Mapped[str]

    resumes: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker"
    )

    resumes_parttime: Mapped[list["ResumesOrm"]] = relationship(
        back_populates="worker",
        primaryjoin="and_(WorkersOrm.id == ResumesOrm.worker_id, ResumesOrm.workload == 'part_time')",
        order_by="ResumesOrm.id.desc()",
    )


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[int_pk]
    title: Mapped[str_255]
    compensation: Mapped[int]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey(
        "workers.id", ondelete="CASCADE")
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    worker: Mapped["WorkersOrm"] = relationship(
        back_populates="resumes"
    )

    vacancies_replied: Mapped[List["VacanciesOrm"]] = relationship(
        back_populates="resumes_replied",
        secondary="vacancies_replies",
    )

    repr_cols_num = 4
    repr_cols = ("created_at", )

    __table_args__ = (
        # PrimaryKeyConstraint("id", "title"),
        Index("title_index", "title"),
        CheckConstraint("compensation > 0", name="check_compensation_positive")
    )


class VacanciesOrm(Base):
    __tablename__ = "vacancies"

    id: Mapped[int_pk]
    title: Mapped[str_255]
    compensation: Mapped[Optional[int]]

    resumes_replied: Mapped[List["ResumesOrm"]] = relationship(
        back_populates="vacancies_replied",
        secondary="vacancies_replies",
    )


class VacanciesRepliesOrm(Base):
    __tablename__ = "vacancies_replies"

    resume_id: Mapped[id] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        primary_key=True,
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE"),
        primary_key=True,
    )

    cover_letter: Mapped[Optional[str]]








workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
