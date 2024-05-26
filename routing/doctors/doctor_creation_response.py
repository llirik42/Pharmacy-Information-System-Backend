from schemas import BaseSchema

from .doctor_creation_status import DoctorCreationStatus


class DoctorCreationResponseSchema(BaseSchema):
    status: DoctorCreationStatus
