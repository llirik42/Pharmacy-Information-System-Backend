from pydantic import Field

from schemas import BaseSchema
from .doctor_creation_status import DoctorCreationStatus


class DoctorCreationResponseSchema(BaseSchema):
    status: DoctorCreationStatus
    doctor_id: int = Field(ge=1, default=0)
