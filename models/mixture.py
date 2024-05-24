from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Mixture(Base):
    __tablename__ = "mixtures"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    solvent: Mapped[str] = mapped_column(String(256))
    mixture_type_id: Mapped[int] = mapped_column(ForeignKey("mixture_types.id"))
