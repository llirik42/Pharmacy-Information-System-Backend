from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DrugOrm(Base):
    __tablename__ = 'drugs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256), unique=True)
    cost: Mapped[int] = mapped_column()
    shelf_life: Mapped[int] = mapped_column()
    critical_amount: Mapped[int] = mapped_column()
    type_id: Mapped[int] = mapped_column(ForeignKey("drug_types.id"))
    description: Mapped[str] = mapped_column(String(256))
