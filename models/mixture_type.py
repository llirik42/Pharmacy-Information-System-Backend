from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class MixtureTypeOrm(Base):
    __tablename__ = "mixture_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256), unique=True)
