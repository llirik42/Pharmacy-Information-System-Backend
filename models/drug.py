from sqlalchemy import String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .drug_type import DrugTypeOrm


class DrugOrm(Base):
    __tablename__ = "drugs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256), unique=True)
    cost: Mapped[int] = mapped_column()
    shelf_life: Mapped[int] = mapped_column()
    critical_amount: Mapped[int] = mapped_column()
    type_id: Mapped[int] = mapped_column(ForeignKey("drug_types.id"))
    description: Mapped[str] = mapped_column(String(256))
    drug_type: Mapped[DrugTypeOrm] = relationship(lazy="joined")

    __table_args__ = (
        CheckConstraint("cost > 0"),
        CheckConstraint("shelf_life > 0"),
        CheckConstraint("critical_amount >= 0"),
    )
