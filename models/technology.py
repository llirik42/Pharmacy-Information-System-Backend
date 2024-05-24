from datetime import time

from sqlalchemy import ForeignKey, CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import Drug
from .technology_component import TechnologyComponent


class Technology(Base):
    __tablename__ = "technologies"

    id: Mapped[int] = mapped_column(primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"))
    cooking_time: Mapped[time] = mapped_column()
    amount: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(String(256))
    drug: Mapped[Drug] = relationship(lazy="joined")
    components: Mapped[list[TechnologyComponent]] = relationship(lazy="joined")

    __table_args__ = (CheckConstraint("amount > 0"),)
