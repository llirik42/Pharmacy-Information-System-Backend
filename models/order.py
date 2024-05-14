from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class OrderOrm(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    prescription_id: Mapped[int] = mapped_column(ForeignKey("prescriptions.id"))
    registration_datetime: Mapped[datetime] = mapped_column()
    appointed_datetime: Mapped[datetime] = mapped_column(nullable=True)
    obtaining_datetime: Mapped[datetime] = mapped_column(nullable=True)
    paid: Mapped[bool] = mapped_column(default=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=True)
