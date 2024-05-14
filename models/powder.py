from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import DrugOrm


class PowderOrm(Base):
    __tablename__ = 'powders'

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    composite: Mapped[bool] = mapped_column()
    drug: Mapped[DrugOrm] = relationship(single_parent=True)
