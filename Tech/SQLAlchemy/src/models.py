from sqlalchemy import Table, Column, UUID, Integer, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


metadata_obj = MetaData()


class WorkersOrm(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]


workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
