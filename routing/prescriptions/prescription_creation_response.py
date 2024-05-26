from schemas import BaseSchema

from .prescription_creation_status import PrescriptionCreationStatus


class PrescriptionCreationResponseSchema(BaseSchema):
    status: PrescriptionCreationStatus
