from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class SalveOrm(Base):
    __tablename__ = "salves"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    active_substance: Mapped[str] = mapped_column(String(256))
