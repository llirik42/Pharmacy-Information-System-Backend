from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PrescriptionItemOrm(Base):
    __tablename__ = 'prescriptions_content'

    prescription_id: Mapped[int] = mapped_column(ForeignKey("prescriptions.id"), primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    amount: Mapped[int] = mapped_column(CheckConstraint("amount > 0"))
    administration_route_id: Mapped[int] = mapped_column(ForeignKey("administration_routes.id"), primary_key=True)
