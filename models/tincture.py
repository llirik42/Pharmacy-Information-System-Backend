from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TinctureOrm(Base):
    __tablename__ = "tinctures"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    material: Mapped[str] = mapped_column(String(256))
