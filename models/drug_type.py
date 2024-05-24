from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class DrugType(Base):
    __tablename__ = "drug_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256), unique=True)
    cookable: Mapped[bool] = mapped_column()
