from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class CustomerOrm(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(256))
    phone_number: Mapped[str] = mapped_column(String(32))
    address: Mapped[str] = mapped_column(String(256))

    __table_args__ = (
        UniqueConstraint('full_name', 'phone_number', 'address'),
    )