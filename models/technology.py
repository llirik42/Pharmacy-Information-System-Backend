from datetime import time

from sqlalchemy import ForeignKey, CheckConstraint, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TechnologyOrm(Base):
    __tablename__ = 'technologies'

    id: Mapped[int] = mapped_column(primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey('drugs.id'))
    cooking_time: Mapped[time] = mapped_column()
    amount: Mapped[int] = mapped_column(CheckConstraint('amount > 0'))
    description: Mapped[str] = mapped_column(String(256))
