from pydantic import Field

from ..base import BaseSchema


class InputPrescriptionItemSchema(BaseSchema):
    drug_id: int
    amount: int = Field(ge=1)
    administration_route_id: int
