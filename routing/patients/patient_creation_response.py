from pydantic import Field

from schemas import BaseSchema
from .patient_creation_status import PatientCreationStatus


class PatientCreationResponseSchema(BaseSchema):
    status: PatientCreationStatus
    patient_id: int = Field(ge=1, default=0)
