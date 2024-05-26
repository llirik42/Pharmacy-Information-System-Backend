from schemas import BaseSchema

from .patient_creation_status import PatientCreationStatus


class PatientCreationResponseSchema(BaseSchema):
    status: PatientCreationStatus
