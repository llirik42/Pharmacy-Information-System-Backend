from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class SupplierOrm(Base):
    __tablename__ = 'suppliers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    phone_number: Mapped[str] = mapped_column(String(32))

    __table_args__ = (
        UniqueConstraint('name', 'phone_number'),
    )
