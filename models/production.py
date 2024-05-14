from datetime import datetime

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ProductionOrm(Base):
    __tablename__ = 'production'

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    technology_id: Mapped[int] = mapped_column(ForeignKey('technologies.id'))
    drug_amount: Mapped[int] = mapped_column(CheckConstraint('drug_amount > 0'))
    start: Mapped[datetime] = mapped_column(nullable=True)
    end: Mapped[datetime] = mapped_column(nullable=True)

    __table_args__ = (
        CheckConstraint('((start is null) and (end is null)) or (end is null) or (end >= start)'),
    )
