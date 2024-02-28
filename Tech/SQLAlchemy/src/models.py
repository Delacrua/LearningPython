import datetime
from typing import Optional, Annotated

from sqlalchemy import Table, Column, UUID, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base, str_255
import enum


metadata_obj = MetaData()


int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
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


class ResumesOrm(Base):
    __tablename__ = "resumes"

    id: Mapped[int_pk]
    title: Mapped[str_255]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey(
        "workers.id", ondelete="CASCADE")
    )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]



workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
