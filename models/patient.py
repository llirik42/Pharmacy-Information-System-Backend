from datetime import date

from sqlalchemy import String, UniqueConstraint, Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(256))
    birthday: Mapped[date] = mapped_column(Date())

    __table_args__ = (UniqueConstraint("full_name", "birthday"),)

    def __repr__(self) -> str:
        return f"{self.full_name}, {self.birthday}"
