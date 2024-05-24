from datetime import date

from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .doctor import Doctor
from .patient import Patient
from .prescription_item import PrescriptionItem


class Prescription(Base):
    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    diagnosis: Mapped[str] = mapped_column(String(512))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    date: Mapped[date] = mapped_column(Date())
    items: Mapped[list[PrescriptionItem]] = relationship(
        lazy="joined",
    )
    patient: Mapped[Patient] = relationship(
        lazy="joined",
    )
    doctor: Mapped[Doctor] = relationship(
        lazy="joined",
    )
