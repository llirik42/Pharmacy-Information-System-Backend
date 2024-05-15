from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PowderOrm(Base):
    __tablename__ = "powders"

    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    composite: Mapped[bool] = mapped_column()
