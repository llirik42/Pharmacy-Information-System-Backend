from pydantic import Field

from schemas import BaseSchema
from .prescription_creation_status import PrescriptionCreationStatus


class PrescriptionCreationResponseSchema(BaseSchema):
    status: PrescriptionCreationStatus
    prescription_id: int = Field(ge=1, default=0)
