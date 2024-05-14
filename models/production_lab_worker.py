from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ProductionLabWorkerOrm(Base):
    __tablename__ = 'production_lab_workers'

    production_id: Mapped[int] = mapped_column(ForeignKey('production.id'), primary_key=True)
    lab_worker_id: Mapped[int] = mapped_column(ForeignKey('lab_workers.id'), primary_key=True)
