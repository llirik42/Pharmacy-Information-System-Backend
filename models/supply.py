from datetime import datetime

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Drug, Supplier
from .base import Base


class Supply(Base):
    __tablename__ = "supplies"

    id: Mapped[int] = mapped_column(primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"))
    drug_amount: Mapped[int] = mapped_column()
    cost: Mapped[int] = mapped_column()
    assigned_datetime: Mapped[datetime] = mapped_column()
    delivery_datetime: Mapped[datetime] = mapped_column(nullable=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"))
    drug: Mapped[Drug] = relationship()
    supplier: Mapped[Supplier] = relationship()

    __table_args__ = (
        CheckConstraint("drug_amount > 0"),
        CheckConstraint("cost >= 0"),
    )
