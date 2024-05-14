from datetime import date

from sqlalchemy import String, ForeignKey, UniqueConstraint, Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PrescriptionOrm(Base):
    __tablename__ = "prescriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    diagnosis: Mapped[str] = mapped_column(String(512))
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"))
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    date: Mapped[date] = mapped_column(Date())

    __table_args__ = (UniqueConstraint("diagnosis", "patient_id", "doctor_id", "date"),)
