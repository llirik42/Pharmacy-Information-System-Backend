from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class LabWorkerOrm(Base):
    __tablename__ = 'lab_workers'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(256), unique=True)
