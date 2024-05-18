from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .administration_route import AdministrationRouteOrm
from .base import Base
from .drug import DrugOrm


class PrescriptionItemOrm(Base):
    __tablename__ = "prescriptions_content"

    prescription_id: Mapped[int] = mapped_column(ForeignKey("prescriptions.id"), primary_key=True)
    drug_id: Mapped[int] = mapped_column(ForeignKey("drugs.id"), primary_key=True)
    amount: Mapped[int] = mapped_column()
    administration_route_id: Mapped[int] = mapped_column(ForeignKey("administration_routes.id"), primary_key=True)
    drug: Mapped[DrugOrm] = relationship(
        lazy="joined",
    )
    administration_route: Mapped[AdministrationRouteOrm] = relationship(
        lazy="joined",
    )

    __table_args__ = (CheckConstraint("amount > 0"),)
