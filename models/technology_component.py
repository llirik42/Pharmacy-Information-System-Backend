from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TechnologyComponentOrm(Base):
    __tablename__ = 'technology_components'

    technology_id: Mapped[int] = mapped_column(ForeignKey('technologies.id'), primary_key=True)
    component_id: Mapped[int] = mapped_column(ForeignKey('drugs.id'), primary_key=True)
    component_amount: Mapped[int] = mapped_column(CheckConstraint('component_amount > 0'))
