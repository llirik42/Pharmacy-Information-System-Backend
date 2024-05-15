from pydantic import BaseModel, Field

from .doctor import Doctor
from .patient import Patient
from .prescription_item import PrescriptionItem
from .base import Base


class Prescription(Base):
    diagnosis: str = Field(max_length=512)
    patient: Patient
    doctor: Doctor
    items: PrescriptionItem
