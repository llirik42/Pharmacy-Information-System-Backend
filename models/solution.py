from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import DrugOrm


class SolutionOrm(Base):
    __tablename__ = 'solutions'

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    dosage: Mapped[int] = mapped_column(CheckConstraint('(0 <= dosage) and (dosage <= 100)'))
    drug: Mapped[DrugOrm] = relationship(single_parent=True)
