from datetime import datetime

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import Drug
from .base import Base


class StorageItem(Base):
    __tablename__ = "storage_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"))
    available_amount: Mapped[int] = mapped_column()
    original_amount: Mapped[int] = mapped_column()
    receipt_datetime: Mapped[datetime] = mapped_column()
    drug: Mapped[Drug] = relationship()

    __table_args__ = (
        CheckConstraint("available_amount >= 0"),
        CheckConstraint("original_amount > 0"),
    )

    def __repr__(self) -> str:
        return f"{self.drug}-{self.original_amount}-{self.receipt_datetime}"
