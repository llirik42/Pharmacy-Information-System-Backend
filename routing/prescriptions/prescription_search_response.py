from typing import Optional

from schemas import BaseSchema, PrescriptionSchema


class PrescriptionSearchResponseSchema(BaseSchema):
    prescription: Optional[PrescriptionSchema] = None
