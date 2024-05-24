from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .customer import Customer
from .prescription import Prescription


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    prescription_id: Mapped[int] = mapped_column(ForeignKey("prescriptions.id"))
    registration_datetime: Mapped[datetime] = mapped_column()
    appointed_datetime: Mapped[datetime] = mapped_column(nullable=True)
    obtaining_datetime: Mapped[datetime] = mapped_column(nullable=True)
    paid: Mapped[bool] = mapped_column(default=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=True, default=None)
    prescription: Mapped[Prescription] = relationship(lazy="joined")
    customer: Mapped[Optional[Customer]] = relationship(lazy="joined")
