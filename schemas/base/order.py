from datetime import datetime
from typing import Optional

from pydantic import Field

from .base import Base
from .customer import Customer
from .prescription import Prescription


class Order(Base):
    id: int = Field(ge=1)
    prescription: Prescription
    registration_datetime: datetime
    appointed_datetime: Optional[datetime] = None
    obtaining_datetime: Optional[datetime] = None
    paid: bool = Field(default=False)
    customer: Optional[Customer] = None
