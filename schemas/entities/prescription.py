import datetime

from pydantic import Field

from .doctor import DoctorSchema
from .patient import PatientSchema
from ..base import BaseSchema
from ..prescription_item import PrescriptionItemSchema


class PrescriptionSchema(BaseSchema):
    id: int = Field(ge=1)
    diagnosis: str = Field(max_length=512)
    patient: PatientSchema
    doctor: DoctorSchema
    date: datetime.date
    items: list[PrescriptionItemSchema]
