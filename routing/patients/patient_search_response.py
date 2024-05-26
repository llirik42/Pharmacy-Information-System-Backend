from typing import Optional

from schemas import BaseSchema, PatientSchema


class PatientSearchResponseSchema(BaseSchema):
    patient: Optional[PatientSchema] = None
