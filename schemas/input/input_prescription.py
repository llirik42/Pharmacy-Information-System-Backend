import datetime

from pydantic import Field

from .input_prescription_item import InputPrescriptionItemSchema
from ..base import BaseSchema


class InputPrescriptionSchema(BaseSchema):
    diagnosis: str = Field(max_length=512)
    patient_id: int = Field(ge=1)
    doctor_id: int = Field(ge=1)
    date: datetime.date
    items: list[InputPrescriptionItemSchema]
