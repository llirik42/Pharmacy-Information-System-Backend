import datetime

from pydantic import Field

from .base import Base
from .doctor import Doctor
from .patient import Patient
from .prescription_item import PrescriptionItem


class Prescription(Base):
    id: int = Field(ge=1)
    diagnosis: str = Field(max_length=512)
    patient: Patient
    doctor: Doctor
    date: datetime.date
    items: list[PrescriptionItem]
