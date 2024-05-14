from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from . import DrugOrm
from .base import Base


class TinctureOrm(Base):
    __tablename__ = "tinctures"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    material: Mapped[str] = mapped_column(String(256))
    drug: Mapped[DrugOrm] = relationship(single_parent=True)
