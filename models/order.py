from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import CustomerOrm
from .base import Base
from .prescription import PrescriptionOrm


class OrderOrm(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    prescription_id: Mapped[int] = mapped_column(ForeignKey("prescriptions.id"))
    registration_datetime: Mapped[datetime] = mapped_column()
    appointed_datetime: Mapped[datetime] = mapped_column(nullable=True)
    obtaining_datetime: Mapped[datetime] = mapped_column(nullable=True)
    paid: Mapped[bool] = mapped_column(default=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=True)
    prescription: Mapped[PrescriptionOrm] = relationship(lazy="joined")
    customer: Mapped[Optional[CustomerOrm]] = relationship(lazy="joined")
