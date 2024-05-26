from datetime import datetime
from typing import Optional

from pydantic import Field

from .customer import CustomerSchema
from .prescription import PrescriptionSchema
from ..base import BaseSchema


class OrderSchema(BaseSchema):
    id: int = Field(ge=1)
    prescription: PrescriptionSchema
    registration_datetime: datetime
    appointed_datetime: Optional[datetime] = None
    obtaining_datetime: Optional[datetime] = None
    paid: bool = Field(default=False)
    customer: Optional[CustomerSchema] = None
