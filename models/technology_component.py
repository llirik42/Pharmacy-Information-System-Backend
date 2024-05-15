from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import DrugOrm


class TechnologyComponentOrm(Base):
    __tablename__ = "technology_components"

    technology_id: Mapped[int] = mapped_column(ForeignKey("technologies.id"), primary_key=True)
    component_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    component_amount: Mapped[int] = mapped_column(CheckConstraint("component_amount > 0"))
    component: Mapped[DrugOrm] = relationship(lazy="joined")
