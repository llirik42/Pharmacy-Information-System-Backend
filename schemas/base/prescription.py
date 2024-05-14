from pydantic import BaseModel, Field

from .patient import Patient
from .doctor import Doctor
from .prescription_item import PrescriptionItem


class Prescription(BaseModel):
    diagnosis: str = Field(max_length=512)
    patient: Patient
    doctor: Doctor
    items: PrescriptionItem
