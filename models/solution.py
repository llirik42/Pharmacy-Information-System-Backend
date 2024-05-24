from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Solution(Base):
    __tablename__ = "solutions"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    dosage: Mapped[int] = mapped_column()

    __table_args__ = (CheckConstraint("(0 <= dosage) and (dosage <= 100)"),)
