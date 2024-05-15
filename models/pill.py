from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PillOrm(Base):
    __tablename__ = "pills"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    weight_of_pill: Mapped[int] = mapped_column(CheckConstraint("weight_of_pill > 0"))
    pills_count: Mapped[int] = mapped_column(CheckConstraint("pills_count > 0"))
