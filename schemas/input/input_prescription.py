import datetime

from pydantic import Field


from ..base import BaseSchema
from .input_prescription_item import InputPrescriptionItemSchema


class InputPrescriptionSchema(BaseSchema):
    diagnosis: str = Field(max_length=512)
    patient_id: int
    doctor_id: int
    date: datetime.date
    items: list[InputPrescriptionItemSchema]
