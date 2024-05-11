from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class DoctorOrm(Base):
    __tablename__ = 'doctors'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(256), nullable=False)
