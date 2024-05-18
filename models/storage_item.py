from datetime import datetime

from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class StorageItemOrm(Base):
    __tablename__ = "storage_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"))
    available_amount: Mapped[int] = mapped_column()
    original_amount: Mapped[int] = mapped_column()
    receipt_datetime: Mapped[datetime] = mapped_column()

    __table_args__ = (
        CheckConstraint("available_amount >= 0"),
        CheckConstraint("original_amount > 0"),
    )
