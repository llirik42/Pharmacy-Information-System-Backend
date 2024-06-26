from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug import Drug


class Salve(Base):
    __tablename__ = "salves"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    active_substance: Mapped[str] = mapped_column(String(256))
    drug: Mapped[Drug] = relationship()
