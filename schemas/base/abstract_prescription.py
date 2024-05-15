from pydantic import Field

from .base import Base
from .doctor import Doctor
from .patient import Patient


class AbstractPrescription(Base):
    diagnosis: str = Field(max_length=512)
    patient: Patient
    doctor: Doctor
