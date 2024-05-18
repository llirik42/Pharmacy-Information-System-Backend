from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class OrderWaitingDrugSupplyOrm(Base):
    __tablename__ = "orders_waiting_drug_supplies"

    order_id: Mapped[int] = mapped_column(ForeignKey("prescriptions.id"), primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    amount: Mapped[int] = mapped_column()

    __table_args__ = (CheckConstraint("amount > 0"),)
