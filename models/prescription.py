from datetime import date

from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .doctor import DoctorOrm
from .patient import PatientOrm
from .prescription_item import PrescriptionItemOrm


class PrescriptionOrm(Base):
    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    diagnosis: Mapped[str] = mapped_column(String(512))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    date: Mapped[date] = mapped_column(Date())
    items: Mapped[list[PrescriptionItemOrm]] = relationship(
        lazy="joined",
    )
    patient: Mapped[PatientOrm] = relationship(
        lazy="joined",
    )
    doctor: Mapped[DoctorOrm] = relationship(
        lazy="joined",
    )
