from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import Drug


class Tincture(Base):
    __tablename__ = "tinctures"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    material: Mapped[str] = mapped_column(String(256))
    drug: Mapped[Drug] = relationship()
