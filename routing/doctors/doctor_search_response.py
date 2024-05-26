from typing import Optional

from schemas import BaseSchema, DoctorSchema


class DoctorSearchResponseSchema(BaseSchema):
    doctor: Optional[DoctorSchema] = None
