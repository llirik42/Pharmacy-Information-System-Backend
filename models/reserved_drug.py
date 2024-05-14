from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ReservedDrugOrm(Base):
    __tablename__ = "reserved_drugs"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    storage_item_id: Mapped[int] = mapped_column(ForeignKey("storage_items.id"), primary_key=True)
    drug_amount: Mapped[int] = mapped_column(CheckConstraint("drug_amount > 0"))
