from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .prescription import Prescription
from .customer import Customer


class Order(BaseModel):
    prescription: Prescription
    registration_datetime: datetime
    appointed_datetime: Optional[datetime] = None
    obtaining_datetime: Optional[datetime] = None
    is_paid: bool = Field(validation_alias='paid')
    customer: Optional[Customer] = None
