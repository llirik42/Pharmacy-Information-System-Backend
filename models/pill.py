from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import Drug


class Pill(Base):
    __tablename__ = "pills"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    weight_of_pill: Mapped[int] = mapped_column()
    pills_count: Mapped[int] = mapped_column()
    drug: Mapped[Drug] = relationship()

    __table_args__ = (
        CheckConstraint("weight_of_pill > 0"),
        CheckConstraint("pills_count > 0"),
    )
